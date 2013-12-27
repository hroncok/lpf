class Handler(object):
    ''' Handle the GUI signals. '''

    def __init__(self):
        global builder

        list_txt = subprocess.check_output(['lpf', 'list'])
        list_pkg = list_text.split('\n')
        table = builder.get_object('main_table')


builder = Gtk.Builder()
main = os.path.dirname(os.path.abspath(__file__)) + "main_window.glade"
builder.add_from_file(main)
builder.connect_signals(Handler())
window=builder.get_object('main_window')
window.show_all()

Gtk.main()
