import auth
from unittest.mock import patch

def test_verify_reset_token_valid():
    token = auth.generate_reset_token("student@uni.edu")
    assert auth.verify_reset_token(token) is True


def test_verify_reset_token_missing():
    assert auth.verify_reset_token("not-a-real-token") is False


def test_verify_reset_token_expired():
    token = auth.generate_reset_token("student@uni.edu", hours_ago=2)
    assert auth.verify_reset_token(token) is False


def test_verify_reset_token_used():
    token = auth.generate_reset_token("student@uni.edu")
    auth.mark_token_used(token)
    assert auth.verify_reset_token(token) is False


def test_check_lockout_allows_below_limit():
    assert auth.check_lockout("student@uni.edu", attempt_count=2) is True


def test_check_lockout_blocks_at_limit():
    assert auth.check_lockout("student@uni.edu", attempt_count=3) is False
    assert auth.is_locked("student@uni.edu") is True


def test_check_lockout_blocks_already_locked_user():
    auth.lock_account("student@uni.edu")
    assert auth.check_lockout("student@uni.edu", attempt_count=0) is False
    # Target: validate_login() email not registered
def test_validate_login_rejects_unregistered_email():
    result = auth.validate_login("ghost@uni.edu", "ValidPass1")
    assert result["success"] is False
    assert result["user_id"] is None
    assert result["error"] == "Invalid credentials"


# Target: validate_login() locked account is refused
def test_validate_login_refuses_locked_account():
    auth.lock_account("student@uni.edu")
    result = auth.validate_login("student@uni.edu", "ValidPass1")
    assert result["success"] is False
    assert result["error"] == "Account is locked"


# Target: validate_login() third wrong password locks the account
def test_validate_login_locks_account_after_three_wrong_passwords():
    for _ in range(3):
        auth.validate_login("student@uni.edu", "WrongPass9")
    assert auth.is_locked("student@uni.edu") is True
    # Target: is_session_valid() no session exists
def test_is_session_valid_returns_false_when_no_session_exists():
    assert auth.is_session_valid("STU-001") is False


# Target: is_session_valid() session idle for 29 minutes
def test_is_session_valid_accepts_29_minute_old_session():
    auth.create_session("STU-001", idle_minutes=29)
    assert auth.is_session_valid("STU-001") is True


# Target: is_session_valid() exactly 30 minute boundary
def test_is_session_valid_rejects_30_minute_old_session():
    auth.create_session("STU-001", idle_minutes=30)
    assert auth.is_session_valid("STU-001") is False


# Target: handle_session() creates a new session
def test_handle_session_creates_new_session():
    assert auth.handle_session("STU-001") is True
    assert auth.is_session_valid("STU-001") is True


# Target: handle_session() rejects expired session
def test_handle_session_rejects_expired_session():
    auth.create_session("STU-001", idle_minutes=45)
    assert auth.handle_session("STU-001") is False


# Target: handle_session() refreshes a valid session
def test_handle_session_refreshes_valid_session():
    auth.create_session("STU-001", idle_minutes=25)

    before = auth.auth_store.sessions["STU-001"]["last_activity"]

    assert auth.handle_session("STU-001") is True

    after = auth.auth_store.sessions["STU-001"]["last_activity"]

    assert after > before
    # Target: send_reset_email() unregistered email
def test_send_reset_email_rejects_unknown_email():
    result = auth.send_reset_email("ghost@uni.edu")
    assert result["sent"] is False
    assert result["error"] == "Email address not found"


# Target: send_reset_email() rate limit after three successful sends
def test_send_reset_email_enforces_rate_limit():
    for _ in range(3):
        result = auth.send_reset_email("student@uni.edu")
        assert result["sent"] is True

    result = auth.send_reset_email("student@uni.edu")
    assert result["sent"] is False
    assert result["error"] == "Rate limit exceeded"


# Target: send_reset_email() token generation failure
def test_send_reset_email_handles_token_generation_failure():
    with patch("auth.generate_reset_token", side_effect=RuntimeError("boom")):
        result = auth.send_reset_email("student@uni.edu")

    assert result["sent"] is False
    assert result["error"] == "Token generation failed: boom"


# Target: send_reset_email() SMTP delivery failure
def test_send_reset_email_handles_smtp_failure():
    with patch("auth._deliver_email", side_effect=ConnectionError("server down")):
        result = auth.send_reset_email("student@uni.edu")

    assert result["sent"] is False
    assert result["error"] == "SMTP error: server down"