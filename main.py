"""Entry point."""

from turtle import ycor
from controllers.base import Controller
from views.base import View


def main():
    view = View()
    controller = Controller(view)
    controller.run()


if __name__ == "__main__":
    main()