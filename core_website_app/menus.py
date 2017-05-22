from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


Menu.add_item(
    "main", MenuItem("Contact", reverse("core_website_app_contact"), icon="envelope", weight=1001)
)

Menu.add_item(
    "main", MenuItem("Help", reverse("core_website_app_help"), icon="question-circle", weight=1002)
)

Menu.add_item(
    "footer", MenuItem("Privacy policy", reverse("core_website_app_privacy"))
)

Menu.add_item(
    "footer", MenuItem("Terms of use", reverse("core_website_app_terms"))
)

# Admin menus for website app
website_children = (
    MenuItem("Privacy Policy", reverse("admin:core_website_app_privacy"), icon="user-secret"),
    MenuItem("Terms of Use", reverse("admin:core_website_app_terms"), icon="file-text-o"),
    MenuItem("Help Page", reverse("admin:core_website_app_help"), icon="question-circle-o"),
    MenuItem("Contact messages", reverse("admin:core_website_app_contact_messages"), icon="envelope"),
)


Menu.add_item(
    "admin", MenuItem("WEBSITE", None, children=website_children)
)

users_menu = [m for m in Menu.items["admin"] if m.title == "USERS"][0]
users_menu_children = list(users_menu.children)
users_menu_children.append(MenuItem("User requests", reverse("admin:core_website_app_user_requests"), icon="user-plus"))
users_menu.children = users_menu_children

