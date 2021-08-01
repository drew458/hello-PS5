import platform


def sendNotification(self):
    """
        Sends a Windows system notifcation.
    """
  
    if platform.system() == "Windows":
        from win10toast import ToastNotifier

        toaster = ToastNotifier()

        global toaster
        toaster.show_toast("FOUND!!!! Go check it out now!")
