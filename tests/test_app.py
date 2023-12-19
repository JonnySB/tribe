from playwright.sync_api import Page, expect
import pytest


# Test get all chants
def test_get_all_chants(page, test_web_address, db_connection):
    db_connection.seed("seeds/tribe.sql")
    page.goto(f"http://{test_web_address}/chants/all")

    messages = page.locator("p.message")

    expect(messages).to_have_text(
        [
            "Chasing dreams!",
            "Having a productive day.",
            "Learning something new every day.",
            "Exploring new ideas.",
            "Coding non-stop!",
            "Enjoying the weekend.",
            "Working on a new project.",
            "Just saying hi!",
            "Feeling great today.",
            "Hello!",
        ]
    )

    timestamps = page.locator("p.date-created")

    expect(timestamps).to_have_text(
        [
            "2023-12-10 22:00:00",
            "2023-12-09 20:10:00",
            "2023-12-08 18:45:00",
            "2023-12-07 16:00:00",
            "2023-12-06 14:30:00",
            "2023-12-05 13:00:00",
            "2023-12-04 11:20:00",
            "2023-12-03 10:15:00",
            "2023-12-02 09:45:00",
            "2023-12-01 08:30:00",
        ]
    )

    users = page.locator("p.author-username")

    expect(users).to_have_text(
        [
            "sophiep_123",
            "maxwell_l",
            "elenagarcia23",
            "bobjohn89",
            "alicesmith_23",
            "sophiep_123",
            "maxwell_l",
            "elenagarcia23",
            "bobjohn89",
            "alicesmith_23",
        ]
    )


def test_link_to_add_user(page, test_web_address, db_connection):
    db_connection.seed("seeds/tribe.sql")
    page.goto(f"http://{test_web_address}/chants/all")
    page.click("text='Add new user'")

    page.fill("input[name=email]", "tomj@exaple.com")
    page.fill("input[name=password]", "password")
    page.fill("input[name=name]", "Tom Jones")
    page.fill("input[name=username]", "tommy_j123")

    page.click("text='submit'")
