from actions.UI_action import UI_action
class WFW_app:

    def logout(self,sidebar):
        UI_action.click_on_elem(sidebar.btn_logout())

    def check_notification(self,sidebar):
        UI_action.click_on_elem(sidebar.btn_notification())

