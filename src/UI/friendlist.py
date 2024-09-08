from PyQt5.QtWidgets import (
   QAction
)
from PyQt5.QtGui import QIcon
import os,sys

#For the Beta?
#Beta Test NR.1
#Test Data

friends = ["Comming Soon!"]
def FriendList(header, menu_bar) -> None:
    friendlist_menu = menu_bar.addMenu(QIcon(os.path.join(sys.path[0], "UI/icons/user.svg")), "")
    llen = len(friends)
    if llen < 1:
       actionf = QAction("No Friends", header)
       actionf.triggered.connect(header.main_window.new_file)
       friendlist_menu.addAction(actionf)
    else:
        if llen > 5:
            others = llen - 5
            for numberf in range(5):
                actionf = QAction(friends[numberf], header)
                actionf.setIcon(QIcon(os.path.join(sys.path[0], "UI/icons/user.svg")))
                actionf.setStatusTip(f"Connect with {friends[numberf]}")
                actionf.triggered.connect(header.main_window.new_file)
                friendlist_menu.addAction(actionf)
            friendlist_menu.addSeparator()
            actionf = QAction(f"{others} More...", header)
            actionf.setIcon(QIcon(os.path.join(sys.path[0], "UI/icons/plus.svg")))
            actionf.triggered.connect(header.main_window.new_file)
            friendlist_menu.addAction(actionf)
        else:
            for friend in friends:
                actionf = QAction(friend, header)
                actionf.setIcon(QIcon(os.path.join(sys.path[0], "UI/icons/user.svg")))
                actionf.setStatusTip(f"Connect with {friend}")
                actionf.triggered.connect(header.main_window.new_file)
                friendlist_menu.addAction(actionf)
    