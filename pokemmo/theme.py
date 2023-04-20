import qdarktheme

PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'
PRIMARY_COLOR_1 = '#f5a5c5'
DARKER_PRIMARY_COLOR_1 = '#e082ab'
DARKEST_PRIMARY_COLOR_1 = '#c35f8f'


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )


qss_pink = f"""
QPushButton[cssClass="specialButtonPink"] {{
color: #fff;
background: {PRIMARY_COLOR_1};
}}
QPushButton[cssClass="specialButtonPink"]:hover {{
color: #fff;
background: {DARKER_PRIMARY_COLOR_1};
}}
QPushButton[cssClass="specialButtonPink"]:pressed {{
color: #fff;
background: {DARKEST_PRIMARY_COLOR_1};
}}
"""
