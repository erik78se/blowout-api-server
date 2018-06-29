import daemon

from oled import main

with daemon.DaemonContext():
    main()
