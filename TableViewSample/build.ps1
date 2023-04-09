" please add *_rc.py when create  all resource files"
pyside6-rcc ui\resource.qrc -o ui\rc_resource.py; 
pyside6-uic ui\main_window.ui -o ui\ui_main_window.py --from-imports --rc-prefix