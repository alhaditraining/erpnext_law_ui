app_name = "erpnext_law_ui"
app_title = "ERPNext Law UI"
app_publisher = "Alhadi Training"
app_description = "Custom UI layer for ERPNext Law Office Management System"
app_email = "support@example.com"
app_license = "MIT"

# Global UI assets for branding and shared styles
app_include_css = [
    "/assets/erpnext_law_ui/css/login.css",
]

app_include_js = [
    "/assets/erpnext_law_ui/js/login.js",
]

# Override the website login page template
website_context = {
    "favicon": "/assets/erpnext_law_ui/images/law-favicon.png",
}
