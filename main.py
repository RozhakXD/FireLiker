import time
from browser.driver import BrowserDriver
from browser.actions import BrowserActions
from models.video import Video
from config import (
    LOGIN_URL, WELCOME_URL, AUTO_VIEWS_URL,
    COOLDOWN_SLEEP, MEDIUM_TIMEOUT
)

class FireLikerBot:
    def __init__(self):
        self.driver = BrowserDriver().initialize_driver()
        self.actions = BrowserActions(self.driver)
        self.selected_video_index = None
        self.video_count = 0

    def run(self):
        """Main execution flow"""
        try:
            self._initial_login()
            self._main_loop()
        except KeyboardInterrupt:
            print("\nBot stopped by user.")
        finally:
            self.driver.quit()

    def _initial_login(self):
        """Handle initial login process"""
        self.actions.navigate_to(LOGIN_URL)
        self.actions.login()

        self.actions.navigate_to(WELCOME_URL)
        self.actions.wait_for_manual_action(
            "Please click 'Continue' on the welcome page..."
        )

    def _main_loop(self):
        """Main bot loop"""
        while True:
            if not self._process_views():
                print("Cooldown detected, waiting...")
                time.sleep(COOLDOWN_SLEEP)
                continue

    def _process_views(self):
        """Process views sending"""
        self.actions.navigate_to(AUTO_VIEWS_URL)

        forms = self.actions.get_forms()
        if not forms:
            print("No videos found.")
            return False

        if self.selected_video_index is None:
            self._select_video(forms)

        if self.selected_video_index >= len(forms):
            print(f"Selected video no longer available (index {self.selected_video_index})")
            self.selected_video_index = None
            return False

        video = Video(forms[self.selected_video_index], self.selected_video_index)
        if not video.select_option():
            print("Failed to select option")
            return False

        if not video.submit():
            print("Failed to submit views")
            return False

        print(f"Successfully sent views for video {self.selected_video_index + 1}")
        time.sleep(MEDIUM_TIMEOUT)
        self.actions.navigate_to(WELCOME_URL + "?info=Views_Send")
        return True

    def _select_video(self, forms):
        """Let user select a video (once at the beginning)"""
        print("\nAvailable videos:")
        for i, form in enumerate(forms):
            video = Video(form, i)
            print(f"{i + 1}. Views: {video.views}")

        while True:
            try:
                choice = int(input(f"Select video (1-{len(forms)}): "))
                if 1 <= choice <= len(forms):
                    self.selected_video_index = choice - 1
                    self.video_count = len(forms)
                    print(f"Selected video {choice} will be used for all subsequent runs")
                    break
                print(f"Please enter number between 1 and {len(forms)}")
            except ValueError:
                print("Please enter a valid number")

if __name__ == "__main__":
    bot = FireLikerBot()
    bot.run()