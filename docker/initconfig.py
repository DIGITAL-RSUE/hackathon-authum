import argparse
import os
import random

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE_EXAMPLE = os.path.join(PROJECT_PATH, ".env.example")
ENV_FILE = os.path.join(PROJECT_PATH, ".env")


class Command:
    """Command init .env file"""

    def get_example_env(self):
        """Get content .env.example"""
        path_example = ENV_FILE_EXAMPLE
        print(path_example)
        example = open(path_example, "r")
        return example.read()

    def generate_secret_key(self):
        """Generate secret key"""
        return "".join(
            [
                random.choice(
                    "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
                )
                for i in range(50)
            ]
        )

    def create_env_file(self, content, is_debug):
        """Create .env file if not exist"""
        path = ENV_FILE
        if not os.path.exists(path):
            env = open(path, "w+")
            env.write(content)
            env.close()

            message = ".env file for production created"

            if is_debug:
                message = ".env file for debug created"

            print(f"  • {message}")
            return

        print("  • .env file already exists")

    def replace_line(self, content, old_value, new_value):
        """Replace line"""
        lines = content.splitlines(True)
        lines = map(
            lambda l: l if old_value not in l else f"{new_value}\n", lines
        )

        return "".join(lines)

    def handle(self, *args, **options):
        is_debug = options["debug"]
        content = self.get_example_env()
        key = self.generate_secret_key()

        content = self.replace_line(
            content, "SECRET_KEY", f"SECRET_KEY='{key}'"
        )

        if is_debug:
            content = self.replace_line(content, "DEBUG", "DEBUG=True")
            content = self.replace_line(
                content, "USE_SQLITE", "USE_SQLITE=False"
            )
            content = self.replace_line(
                content,
                "USE_FILE_EMAIL_BACKEND",
                "USE_FILE_EMAIL_BACKEND=True",
            )
            content = self.replace_line(
                content, "SITE_DOMAIN", "SITE_DOMAIN='*'"
            )
            content = self.replace_line(
                content, "DEV_IN_DOCKER", f"DEV_IN_DOCKER={options['docker']}"
            )
            content = self.replace_line(
                content,
                "DATABASE_URL",
                "DATABASE_URL='pgsql://postgres:postgres@db:5432/postgres'",
            )
        self.create_env_file(content, is_debug)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="debug mode", action="store_true")
    parser.add_argument("--docker", help="docker mode", action="store_true")
    args = parser.parse_args()
    Command().handle(**vars(args))
