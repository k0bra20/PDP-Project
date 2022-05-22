screen_helper = """
ScreenManager:
    WelcomeScreen:
    MainScreen:
    AlarmScreen:
    QuoteScreen:
    SecondQuoteScreen:

<WelcomeScreen>:
    name : 'welcome'
    MDBoxLayout:
        # Add float layout
        MDFloatLayout:
            # Add Gif image
            Image:
                source:'assets/loveandjoy.gif'
                allow_stretch: True
                anim_delay: 0.08
                # anim_loop: 4
                anim_reset: False
            MDRectangleFlatButton:
                text:'Setup the quote theme and the alarm'
                halign: 'center'
                pos_hint:{'center_x':0.5,'center_y':0.1}
                on_press: root.manager.current = 'main'


<MainScreen>:
    name: 'main'
    MDRectangleFlatButton:
        text: 'alarm'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'alarm'
    MDRectangleFlatButton:
        text: 'quote'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'quote'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Alarm & Quote'
            left_action_items: [["clock"]]
            elevation: 13
     
    MDBottomAppBar:
        MDToolbar:
            title:'Support'
            left_action_items: [["help"]]
            mode: 'end'
            type: 'bottom'
            icon: 'window-close'
            on_action_button: app.close_application()

<AlarmScreen>:
    name: 'alarm'
    MDFloatLayout:
        md_Bg_color: 1,1,1,1
        MDLabel:
            text: "ALARM"
            font_size:"30sp"
            pos_hint: {"center_y": .935}
            halign: "center"
            bold: True
        MDIconButton:
            icon: "plus"
            pos_hint:{"center_x": .87, "center_y": .94}
            md_bg_color: 0,0,0,1
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            on_release: root.time_picker()
        MDLabel:
            id: alarm_time
            text: ""
            pos_hint: {"center_y": .5}
            halign:"center"
            font_size: "30sp"
            bold: True

            
        MDIconButton:
            icon: 'keyboard-backspace'
            pos_hint: {'center_x':0.1,'center_y':0.93}
            on_press: root.manager.current = 'main'    
            
        MDRectangleFlatButton:
            text: 'Open the quote if you want shut the chicken !!'
            pos_hint: {'center_x':0.5,'center_y':0.4}
            on_release: root.show_alert_dialog()
            

    MDBottomAppBar:
        MDToolbar:
            title:'Support'
            left_action_items: [["help"]]
            mode: 'end'
            type: 'bottom'
            icon: 'window-close'
            on_action_button: app.close_application()
    
<QuoteScreen>:
    name: 'quote'
    MDFloatLayout:
        md_Bg_color: 1,1,1,1
        MDLabel:
            text: "QUOTES"
            font_size:"30sp"
            pos_hint: {"center_y": .935}
            halign: "center"
            bold: True
    MDRaisedButton:
        text:'what type of quotes are you looking for?'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None    
        width:265
        on_press: root.manager.current = 'second_quote'
    MDIconButton:
        icon: 'keyboard-backspace'
        pos_hint: {'center_x':0.1,'center_y':0.93}
        on_press: root.manager.current = 'main'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Alarm & Quote'
            left_action_items: [["clock"]]
            elevation: 13

    MDBottomAppBar:
        MDToolbar:
            title:'Support'
            left_action_items: [["help"]]
            mode: 'end'
            type: 'bottom'
            icon: 'window-close'
            on_action_button: app.close_application()
            
<SecondQuoteScreen>:
    name:'second_quote'
    MDFloatLayout:
        md_Bg_color: 1,1,1,1
        MDLabel:
            text: "QUOTES"
            font_size:"30sp"
            pos_hint: {"center_y": .935}
            halign: "center"
            bold: True

    Spinner:
        id: spinner_id
        size_hint: None, None
        size:200, 80
        pos_hint:{'center':(.5,.8)}
        text:'Categories'
        values:['ability','age','advice','adversity','amazing','anger','animals','anniversary','architecture','art','attitude','beauty','best','birthday','boldness','business','car','change','charity','children','creation','communication','computers','cool','courage','dad','dating','death','design','destiny','diet','discretion','doubt','dreams','education','enemy','enthusiasm','environmental','envy','equality','evil','experience','exploration','failure','fate','faith','fame','family','famous','fear','finance','fitness','food','forgiveness','freedom','friendship','funny','future','gardening','god','good','government','graduation','great','grief','happiness','health','history','home','honesty','hope','humor','hypocrisy','idea','imagination','individuality','inspirational','intelligence','jealousy','judgment','kindness','knowledge','law','leadership','learning','legal','life','love','marriage','medical','meditation','men','mom','money','morning','movies','music','opinion','pain','politics','pride','reflection','religion','risk','selfishness','silence','solitude','soul','success','taste']
        on_text: root.spinner_clicked()

    MDIconButton:
        icon: 'keyboard-backspace'
        pos_hint: {'center_x':0.1,'center_y':0.93}
        on_press: root.manager.current = 'main'

    
"""
