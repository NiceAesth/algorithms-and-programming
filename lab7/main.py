from __future__ import annotations

import classes


def main() -> None:
    """Main function. Runs a menu."""
    menu = classes.MainMenu(classes.AppManager())

    menu.run()


if __name__ == "__main__":
    main()
