from auth import register_user, login


def test_login_ok():
    register_user("a@b.com", "pass")
    assert login("a@b.com", "pass")


def test_login_wrong_password():
    register_user("c@d.com", "pass")
    assert not login("c@d.com", "sai")
