class ValidationError(Exception):
    pass


def validate_user(user):
    """Check that a user record can log in."""
    if user is None:
        raise ValidationError("no user")
    if not user.get("email"):
        raise ValidationError("email is required")
    if user.get("disabled"):
        raise ValidationError("account disabled")
    return True


def login(user, password, check_password):
    validate_user(user)
    if not check_password(user, password):
        raise ValidationError("bad credentials")
    return {"user": user["email"], "ok": True}
