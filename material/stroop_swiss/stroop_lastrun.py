#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Fri Oct 21 07:20:35 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard





# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'stroop'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '01',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/thomasquettier/Library/Mobile Documents/com~apple~CloudDocs/01.WORK/09.arcapy/github/course-psychopy3/material/stroop_swiss/stroop_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "SETTING"
SETTINGClock = core.Clock()
# parametters

fixation_duration = 0.5

rep_condition = 1 # nb rep per blocchi sperimentali



# nb rep blocchi sperimentali
num = (int(expInfo['participant']) % 2)

if  num == 0:
    nb_rep_ita = 1*rep_condition
    nb_rep_eng = 0 
    blocco_order = "ITA_ENG"
else:
    nb_rep_eng = 1*rep_condition   
    nb_rep_ita = 0
    blocco_order = "ENG_ITA"


# Initialize components for Routine "HUMAN"
HUMANClock = core.Clock()
human_txt = visual.TextStim(win=win, name='human_txt',
    text='Scrivi il risultato:',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
math_txt = visual.TextStim(win=win, name='math_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.2),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
button = visual.ButtonStim(win, 
    text='validare', font='Arvo',
    pos=(0, -0.7),
    letterHeight=0.05,
    size=(0.2,0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()

# Initialize components for Routine "MATRIX"
MATRIXClock = core.Clock()
blue_img = visual.ImageStim(
    win=win,
    name='blue_img', units='pix', 
    image='images/blue_pill.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-250, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
red_img = visual.ImageStim(
    win=win,
    name='red_img', units='pix', 
    image='images/red_pill.jpg', mask=None, anchor='center',
    ori=0.0, pos=(250, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
practice_ms = event.Mouse(win=win)
x, y = [None, None]
practice_ms.mouseClock = core.Clock()

# Initialize components for Routine "ISTR_PRACTICE"
ISTR_PRACTICEClock = core.Clock()
istr_practice_txt = visual.TextStim(win=win, name='istr_practice_txt',
    text="Per favore, premi la freccia;\nSINISTRA se il colore è ROSSO\nBASSA se il colore è VERDE\nDESTRA se il colore è BLU\n\nInitiamo con un po' di pratica\n\nPremi qualsiasi tasto per iniziare",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
istr_practice_kb = keyboard.Keyboard()

# Initialize components for Routine "FIXATION"
FIXATIONClock = core.Clock()
fixation_txt = visual.TextStim(win=win, name='fixation_txt',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TRIAL_PRACTICE"
TRIAL_PRACTICEClock = core.Clock()


practice_txt = visual.TextStim(win=win, name='practice_txt',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
practice_kb = keyboard.Keyboard()

# Initialize components for Routine "FEEDBACK"
FEEDBACKClock = core.Clock()
# initialisation di variabili 
msg = '' # per FEEDBACK
endpractice = [] # per uscire di practice loop
feedback_txt = visual.TextStim(win=win, name='feedback_txt',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ISTR_ESPERIMENTO"
ISTR_ESPERIMENTOClock = core.Clock()
istr_esperimento_txt = visual.TextStim(win=win, name='istr_esperimento_txt',
    text="Ottimo,\n\nAdesso iniziamo l'esperimento, ricordati di premere:\nSINISTRA se il colore è ROSSO\nBASSO se il colore è VERDE\nDESTRA se il colore è BLU\n\n\nPremi qualsiasi tasto per iniziare",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
istr_esperimento_kb = keyboard.Keyboard()

# Initialize components for Routine "FIXATION"
FIXATIONClock = core.Clock()
fixation_txt = visual.TextStim(win=win, name='fixation_txt',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TRIAL_ITA"
TRIAL_ITAClock = core.Clock()


ita_txt = visual.TextStim(win=win, name='ita_txt',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ita_kb = keyboard.Keyboard()

# Initialize components for Routine "FIXATION"
FIXATIONClock = core.Clock()
fixation_txt = visual.TextStim(win=win, name='fixation_txt',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TRIAL_ENG"
TRIAL_ENGClock = core.Clock()
eng_txt = visual.TextStim(win=win, name='eng_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eng_kb = keyboard.Keyboard()

# Initialize components for Routine "SWITCH"
SWITCHClock = core.Clock()

# Initialize components for Routine "LIKERT"
LIKERTClock = core.Clock()
likert_txt = visual.TextStim(win=win, name='likert_txt',
    text='Da 1 a 10, quanto pensi di essere stato accurato nelle tue risposte ?',
    font='Open Sans',
    pos=(0, 0.5), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
likert_sld = visual.Slider(win=win, name='likert_sld',
    startValue=5, size=(1.0, 0.05), pos=(0, 0), units=None,
    labels=["per niente accurato","molto accurato"], ticks=(1, 2, 3, 4, 5,6,7,8,9,10), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)
likert_bt = visual.ButtonStim(win, 
    text='premi per prosseguire', font='Arvo',
    pos=(0, -0.5),
    letterHeight=0.05,
    size=(0.3,0.15), borderWidth=0.0,
    fillColor='white', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='likert_bt'
)
likert_bt.buttonClock = core.Clock()

# Initialize components for Routine "GRAZIE"
GRAZIEClock = core.Clock()
logo_img = visual.ImageStim(
    win=win,
    name='logo_img', units='pix', 
    image='images/logo.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 150), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
grazie_txt = visual.TextStim(win=win, name='grazie_txt',
    text="L'esperimento è finito.\n\nGrazie!",
    font='arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
grazie_kb = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "SETTING"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
SETTINGComponents = []
for thisComponent in SETTINGComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SETTINGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SETTING"-------
while continueRoutine:
    # get current time
    t = SETTINGClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SETTINGClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SETTINGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SETTING"-------
for thisComponent in SETTINGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "SETTING" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
HumanLoop = data.TrialHandler(nReps=100.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='HumanLoop')
thisExp.addLoop(HumanLoop)  # add the loop to the experiment
thisHumanLoop = HumanLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHumanLoop.rgb)
if thisHumanLoop != None:
    for paramName in thisHumanLoop:
        exec('{} = thisHumanLoop[paramName]'.format(paramName))

for thisHumanLoop in HumanLoop:
    currentLoop = HumanLoop
    # abbreviate parameter names if possible (e.g. rgb = thisHumanLoop.rgb)
    if thisHumanLoop != None:
        for paramName in thisHumanLoop:
            exec('{} = thisHumanLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "HUMAN"-------
    continueRoutine = True
    # update component parameters for each repeat
    x = int(random()*10)    # numpy random number tra 1 e 100.
    y = int(random()*10) 
    
    correctsum = x+y
    
    math = str(x) + " + " + str(y) + " ="
    math_txt.setText(math)
    textbox.reset()
    # keep track of which components have finished
    HUMANComponents = [human_txt, math_txt, textbox, button]
    for thisComponent in HUMANComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    HUMANClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "HUMAN"-------
    while continueRoutine:
        # get current time
        t = HUMANClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=HUMANClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        
        # *human_txt* updates
        if human_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            human_txt.frameNStart = frameN  # exact frame index
            human_txt.tStart = t  # local t and not account for scr refresh
            human_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(human_txt, 'tStartRefresh')  # time at next scr refresh
            human_txt.setAutoDraw(True)
        
        # *math_txt* updates
        if math_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            math_txt.frameNStart = frameN  # exact frame index
            math_txt.tStart = t  # local t and not account for scr refresh
            math_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_txt, 'tStartRefresh')  # time at next scr refresh
            math_txt.setAutoDraw(True)
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        
        # *button* updates
        if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            button.setAutoDraw(True)
        if button.status == STARTED:
            # check whether button has been pressed
            if button.isClicked:
                if not button.wasClicked:
                    button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                    button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
                else:
                    button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
                if not button.wasClicked:
                    continueRoutine = False  # end routine when button is clicked
                    None
                button.wasClicked = True  # if button is still clicked next frame, it is not a new click
            else:
                button.wasClicked = False  # if button is clicked next frame, it is a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HUMANComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "HUMAN"-------
    for thisComponent in HUMANComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if str(correctsum) == textbox.text:
            HumanLoop.finished = True
    
    HumanLoop.addData('human_txt.started', human_txt.tStartRefresh)
    HumanLoop.addData('human_txt.stopped', human_txt.tStopRefresh)
    HumanLoop.addData('math_txt.started', math_txt.tStartRefresh)
    HumanLoop.addData('math_txt.stopped', math_txt.tStopRefresh)
    HumanLoop.addData('textbox.text',textbox.text)
    HumanLoop.addData('textbox.started', textbox.tStartRefresh)
    HumanLoop.addData('textbox.stopped', textbox.tStopRefresh)
    HumanLoop.addData('button.started', button.tStartRefresh)
    HumanLoop.addData('button.stopped', button.tStopRefresh)
    HumanLoop.addData('button.numClicks', button.numClicks)
    if button.numClicks:
       HumanLoop.addData('button.timesOn', button.timesOn)
       HumanLoop.addData('button.timesOff', button.timesOff)
    else:
       HumanLoop.addData('button.timesOn', "")
       HumanLoop.addData('button.timesOff', "")
    # the Routine "HUMAN" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 100.0 repeats of 'HumanLoop'


# ------Prepare to start Routine "MATRIX"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the practice_ms
practice_ms.x = []
practice_ms.y = []
practice_ms.leftButton = []
practice_ms.midButton = []
practice_ms.rightButton = []
practice_ms.time = []
practice_ms.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
MATRIXComponents = [blue_img, red_img, practice_ms]
for thisComponent in MATRIXComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MATRIXClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MATRIX"-------
while continueRoutine:
    # get current time
    t = MATRIXClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MATRIXClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blue_img* updates
    if blue_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blue_img.frameNStart = frameN  # exact frame index
        blue_img.tStart = t  # local t and not account for scr refresh
        blue_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blue_img, 'tStartRefresh')  # time at next scr refresh
        blue_img.setAutoDraw(True)
    
    # *red_img* updates
    if red_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_img.frameNStart = frameN  # exact frame index
        red_img.tStart = t  # local t and not account for scr refresh
        red_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_img, 'tStartRefresh')  # time at next scr refresh
        red_img.setAutoDraw(True)
    # *practice_ms* updates
    if practice_ms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_ms.frameNStart = frameN  # exact frame index
        practice_ms.tStart = t  # local t and not account for scr refresh
        practice_ms.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_ms, 'tStartRefresh')  # time at next scr refresh
        practice_ms.status = STARTED
        practice_ms.mouseClock.reset()
        prevButtonState = practice_ms.getPressed()  # if button is down already this ISN'T a new click
    if practice_ms.status == STARTED:  # only update if started and not finished!
        buttons = practice_ms.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([blue_img, red_img])
                    clickableList = [blue_img, red_img]
                except:
                    clickableList = [[blue_img, red_img]]
                for obj in clickableList:
                    if obj.contains(practice_ms):
                        gotValidClick = True
                        practice_ms.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = practice_ms.getPos()
                    practice_ms.x.append(x)
                    practice_ms.y.append(y)
                    buttons = practice_ms.getPressed()
                    practice_ms.leftButton.append(buttons[0])
                    practice_ms.midButton.append(buttons[1])
                    practice_ms.rightButton.append(buttons[2])
                    practice_ms.time.append(practice_ms.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MATRIXComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MATRIX"-------
for thisComponent in MATRIXComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# decisione se fare il blocco pratica o meno:
if practice_ms.clicked_name[0] == "blue_img":
    practice = 1 #blue pill = fare pratica
else:
    practice = 0 #red pill = no pratica

# store data for thisExp (ExperimentHandler)
thisExp.addData('practice_ms.x', practice_ms.x)
thisExp.addData('practice_ms.y', practice_ms.y)
thisExp.addData('practice_ms.leftButton', practice_ms.leftButton)
thisExp.addData('practice_ms.midButton', practice_ms.midButton)
thisExp.addData('practice_ms.rightButton', practice_ms.rightButton)
thisExp.addData('practice_ms.time', practice_ms.time)
thisExp.addData('practice_ms.clicked_name', practice_ms.clicked_name)
thisExp.addData('practice_ms.started', practice_ms.tStartRefresh)
thisExp.addData('practice_ms.stopped', practice_ms.tStopRefresh)
thisExp.nextEntry()
# the Routine "MATRIX" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
FullPracticeLoop = data.TrialHandler(nReps=practice, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='FullPracticeLoop')
thisExp.addLoop(FullPracticeLoop)  # add the loop to the experiment
thisFullPracticeLoop = FullPracticeLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFullPracticeLoop.rgb)
if thisFullPracticeLoop != None:
    for paramName in thisFullPracticeLoop:
        exec('{} = thisFullPracticeLoop[paramName]'.format(paramName))

for thisFullPracticeLoop in FullPracticeLoop:
    currentLoop = FullPracticeLoop
    # abbreviate parameter names if possible (e.g. rgb = thisFullPracticeLoop.rgb)
    if thisFullPracticeLoop != None:
        for paramName in thisFullPracticeLoop:
            exec('{} = thisFullPracticeLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ISTR_PRACTICE"-------
    continueRoutine = True
    # update component parameters for each repeat
    istr_practice_kb.keys = []
    istr_practice_kb.rt = []
    _istr_practice_kb_allKeys = []
    # keep track of which components have finished
    ISTR_PRACTICEComponents = [istr_practice_txt, istr_practice_kb]
    for thisComponent in ISTR_PRACTICEComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISTR_PRACTICEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISTR_PRACTICE"-------
    while continueRoutine:
        # get current time
        t = ISTR_PRACTICEClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISTR_PRACTICEClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *istr_practice_txt* updates
        if istr_practice_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            istr_practice_txt.frameNStart = frameN  # exact frame index
            istr_practice_txt.tStart = t  # local t and not account for scr refresh
            istr_practice_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(istr_practice_txt, 'tStartRefresh')  # time at next scr refresh
            istr_practice_txt.setAutoDraw(True)
        
        # *istr_practice_kb* updates
        if istr_practice_kb.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            istr_practice_kb.frameNStart = frameN  # exact frame index
            istr_practice_kb.tStart = t  # local t and not account for scr refresh
            istr_practice_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(istr_practice_kb, 'tStartRefresh')  # time at next scr refresh
            istr_practice_kb.status = STARTED
            # keyboard checking is just starting
            istr_practice_kb.clock.reset()  # now t=0
            istr_practice_kb.clearEvents(eventType='keyboard')
        if istr_practice_kb.status == STARTED:
            theseKeys = istr_practice_kb.getKeys(keyList=None, waitRelease=False)
            _istr_practice_kb_allKeys.extend(theseKeys)
            if len(_istr_practice_kb_allKeys):
                istr_practice_kb.keys = _istr_practice_kb_allKeys[-1].name  # just the last key pressed
                istr_practice_kb.rt = _istr_practice_kb_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISTR_PRACTICEComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISTR_PRACTICE"-------
    for thisComponent in ISTR_PRACTICEComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISTR_PRACTICE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    PracticeLoop = data.TrialHandler(nReps=10.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condizione.xlsx'),
        seed=None, name='PracticeLoop')
    thisExp.addLoop(PracticeLoop)  # add the loop to the experiment
    thisPracticeLoop = PracticeLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    for thisPracticeLoop in PracticeLoop:
        currentLoop = PracticeLoop
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
        if thisPracticeLoop != None:
            for paramName in thisPracticeLoop:
                exec('{} = thisPracticeLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FIXATION"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FIXATIONComponents = [fixation_txt]
        for thisComponent in FIXATIONComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FIXATIONClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FIXATION"-------
        while continueRoutine:
            # get current time
            t = FIXATIONClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FIXATIONClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_txt* updates
            if fixation_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_txt.frameNStart = frameN  # exact frame index
                fixation_txt.tStart = t  # local t and not account for scr refresh
                fixation_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_txt, 'tStartRefresh')  # time at next scr refresh
                fixation_txt.setAutoDraw(True)
            if fixation_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_txt.tStartRefresh + fixation_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_txt.tStop = t  # not accounting for scr refresh
                    fixation_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_txt, 'tStopRefresh')  # time at next scr refresh
                    fixation_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FIXATIONComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FIXATION"-------
        for thisComponent in FIXATIONComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracticeLoop.addData('fixation_txt.started', fixation_txt.tStartRefresh)
        PracticeLoop.addData('fixation_txt.stopped', fixation_txt.tStopRefresh)
        # the Routine "FIXATION" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "TRIAL_PRACTICE"-------
        continueRoutine = True
        # update component parameters for each repeat
        practice_txt.setColor(colore, colorSpace='rgb')
        practice_txt.setText(parola)
        practice_kb.keys = []
        practice_kb.rt = []
        _practice_kb_allKeys = []
        # keep track of which components have finished
        TRIAL_PRACTICEComponents = [practice_txt, practice_kb]
        for thisComponent in TRIAL_PRACTICEComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TRIAL_PRACTICEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TRIAL_PRACTICE"-------
        while continueRoutine:
            # get current time
            t = TRIAL_PRACTICEClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TRIAL_PRACTICEClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_txt* updates
            if practice_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                practice_txt.frameNStart = frameN  # exact frame index
                practice_txt.tStart = t  # local t and not account for scr refresh
                practice_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_txt, 'tStartRefresh')  # time at next scr refresh
                practice_txt.setAutoDraw(True)
            
            # *practice_kb* updates
            waitOnFlip = False
            if practice_kb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                practice_kb.frameNStart = frameN  # exact frame index
                practice_kb.tStart = t  # local t and not account for scr refresh
                practice_kb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_kb, 'tStartRefresh')  # time at next scr refresh
                practice_kb.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_kb.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practice_kb.status == STARTED and not waitOnFlip:
                theseKeys = practice_kb.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
                _practice_kb_allKeys.extend(theseKeys)
                if len(_practice_kb_allKeys):
                    practice_kb.keys = _practice_kb_allKeys[-1].name  # just the last key pressed
                    practice_kb.rt = _practice_kb_allKeys[-1].rt
                    # was this correct?
                    if (practice_kb.keys == str(corrAns)) or (practice_kb.keys == corrAns):
                        practice_kb.corr = 1
                    else:
                        practice_kb.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TRIAL_PRACTICEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TRIAL_PRACTICE"-------
        for thisComponent in TRIAL_PRACTICEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("blocco", "PRACTICE")
        thisExp.addData("order", blocco_order)
        PracticeLoop.addData('practice_txt.started', practice_txt.tStartRefresh)
        PracticeLoop.addData('practice_txt.stopped', practice_txt.tStopRefresh)
        # check responses
        if practice_kb.keys in ['', [], None]:  # No response was made
            practice_kb.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               practice_kb.corr = 1;  # correct non-response
            else:
               practice_kb.corr = 0;  # failed to respond (incorrectly)
        # store data for PracticeLoop (TrialHandler)
        PracticeLoop.addData('practice_kb.keys',practice_kb.keys)
        PracticeLoop.addData('practice_kb.corr', practice_kb.corr)
        if practice_kb.keys != None:  # we had a response
            PracticeLoop.addData('practice_kb.rt', practice_kb.rt)
        PracticeLoop.addData('practice_kb.started', practice_kb.tStartRefresh)
        PracticeLoop.addData('practice_kb.stopped', practice_kb.tStopRefresh)
        # the Routine "TRIAL_PRACTICE" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "FEEDBACK"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # "resp_kb.corr" è ottenuto se trial 
        # routine  "resp_kb" registra la risposta correta
        
        if practice_kb.corr: 
          msg="Bravo! RT=%.3f" %(practice_kb.rt)
          #msg = "Correct! RT={:.3f}".format(resp_kb.rt)
        
        else:
          msg="Oops! non è coretto"
        
        
        feedback_txt.setText(msg)
        # keep track of which components have finished
        FEEDBACKComponents = [feedback_txt]
        for thisComponent in FEEDBACKComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FEEDBACKClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FEEDBACK"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FEEDBACKClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FEEDBACKClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_txt* updates
            if feedback_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_txt.frameNStart = frameN  # exact frame index
                feedback_txt.tStart = t  # local t and not account for scr refresh
                feedback_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_txt, 'tStartRefresh')  # time at next scr refresh
                feedback_txt.setAutoDraw(True)
            if feedback_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_txt.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_txt.tStop = t  # not accounting for scr refresh
                    feedback_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_txt, 'tStopRefresh')  # time at next scr refresh
                    feedback_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FEEDBACKComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FEEDBACK"-------
        for thisComponent in FEEDBACKComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # track (up to) the last 5 trials
        endpractice.append(practice_kb.corr)
        
        # en practice loop se 4 risposte corr nelle ultime 6
        if sum(endpractice[-6:] ) == 4:
            PracticeLoop.finished = True
        
        
        
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'PracticeLoop'
    
    # get names of stimulus parameters
    if PracticeLoop.trialList in ([], [None], None):
        params = []
    else:
        params = PracticeLoop.trialList[0].keys()
    # save data for this loop
    PracticeLoop.saveAsExcel(filename + '.xlsx', sheetName='PracticeLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed practice repeats of 'FullPracticeLoop'


# set up handler to look after randomisation of conditions etc
ControbilanciamewntoLoop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ControbilanciamewntoLoop')
thisExp.addLoop(ControbilanciamewntoLoop)  # add the loop to the experiment
thisControbilanciamewntoLoop = ControbilanciamewntoLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisControbilanciamewntoLoop.rgb)
if thisControbilanciamewntoLoop != None:
    for paramName in thisControbilanciamewntoLoop:
        exec('{} = thisControbilanciamewntoLoop[paramName]'.format(paramName))

for thisControbilanciamewntoLoop in ControbilanciamewntoLoop:
    currentLoop = ControbilanciamewntoLoop
    # abbreviate parameter names if possible (e.g. rgb = thisControbilanciamewntoLoop.rgb)
    if thisControbilanciamewntoLoop != None:
        for paramName in thisControbilanciamewntoLoop:
            exec('{} = thisControbilanciamewntoLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ISTR_ESPERIMENTO"-------
    continueRoutine = True
    # update component parameters for each repeat
    istr_esperimento_kb.keys = []
    istr_esperimento_kb.rt = []
    _istr_esperimento_kb_allKeys = []
    # keep track of which components have finished
    ISTR_ESPERIMENTOComponents = [istr_esperimento_txt, istr_esperimento_kb]
    for thisComponent in ISTR_ESPERIMENTOComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISTR_ESPERIMENTOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISTR_ESPERIMENTO"-------
    while continueRoutine:
        # get current time
        t = ISTR_ESPERIMENTOClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISTR_ESPERIMENTOClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *istr_esperimento_txt* updates
        if istr_esperimento_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            istr_esperimento_txt.frameNStart = frameN  # exact frame index
            istr_esperimento_txt.tStart = t  # local t and not account for scr refresh
            istr_esperimento_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(istr_esperimento_txt, 'tStartRefresh')  # time at next scr refresh
            istr_esperimento_txt.setAutoDraw(True)
        
        # *istr_esperimento_kb* updates
        if istr_esperimento_kb.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            istr_esperimento_kb.frameNStart = frameN  # exact frame index
            istr_esperimento_kb.tStart = t  # local t and not account for scr refresh
            istr_esperimento_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(istr_esperimento_kb, 'tStartRefresh')  # time at next scr refresh
            istr_esperimento_kb.status = STARTED
            # keyboard checking is just starting
            istr_esperimento_kb.clock.reset()  # now t=0
            istr_esperimento_kb.clearEvents(eventType='keyboard')
        if istr_esperimento_kb.status == STARTED:
            theseKeys = istr_esperimento_kb.getKeys(keyList=None, waitRelease=False)
            _istr_esperimento_kb_allKeys.extend(theseKeys)
            if len(_istr_esperimento_kb_allKeys):
                istr_esperimento_kb.keys = _istr_esperimento_kb_allKeys[-1].name  # just the last key pressed
                istr_esperimento_kb.rt = _istr_esperimento_kb_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISTR_ESPERIMENTOComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISTR_ESPERIMENTO"-------
    for thisComponent in ISTR_ESPERIMENTOComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISTR_ESPERIMENTO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ItaLoop = data.TrialHandler(nReps=nb_rep_ita, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condizione.xlsx'),
        seed=None, name='ItaLoop')
    thisExp.addLoop(ItaLoop)  # add the loop to the experiment
    thisItaLoop = ItaLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisItaLoop.rgb)
    if thisItaLoop != None:
        for paramName in thisItaLoop:
            exec('{} = thisItaLoop[paramName]'.format(paramName))
    
    for thisItaLoop in ItaLoop:
        currentLoop = ItaLoop
        # abbreviate parameter names if possible (e.g. rgb = thisItaLoop.rgb)
        if thisItaLoop != None:
            for paramName in thisItaLoop:
                exec('{} = thisItaLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FIXATION"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FIXATIONComponents = [fixation_txt]
        for thisComponent in FIXATIONComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FIXATIONClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FIXATION"-------
        while continueRoutine:
            # get current time
            t = FIXATIONClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FIXATIONClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_txt* updates
            if fixation_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_txt.frameNStart = frameN  # exact frame index
                fixation_txt.tStart = t  # local t and not account for scr refresh
                fixation_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_txt, 'tStartRefresh')  # time at next scr refresh
                fixation_txt.setAutoDraw(True)
            if fixation_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_txt.tStartRefresh + fixation_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_txt.tStop = t  # not accounting for scr refresh
                    fixation_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_txt, 'tStopRefresh')  # time at next scr refresh
                    fixation_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FIXATIONComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FIXATION"-------
        for thisComponent in FIXATIONComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ItaLoop.addData('fixation_txt.started', fixation_txt.tStartRefresh)
        ItaLoop.addData('fixation_txt.stopped', fixation_txt.tStopRefresh)
        # the Routine "FIXATION" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "TRIAL_ITA"-------
        continueRoutine = True
        # update component parameters for each repeat
        ita_txt.setColor(colore, colorSpace='rgb')
        ita_txt.setText(parola)
        ita_kb.keys = []
        ita_kb.rt = []
        _ita_kb_allKeys = []
        # keep track of which components have finished
        TRIAL_ITAComponents = [ita_txt, ita_kb]
        for thisComponent in TRIAL_ITAComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TRIAL_ITAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TRIAL_ITA"-------
        while continueRoutine:
            # get current time
            t = TRIAL_ITAClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TRIAL_ITAClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ita_txt* updates
            if ita_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                ita_txt.frameNStart = frameN  # exact frame index
                ita_txt.tStart = t  # local t and not account for scr refresh
                ita_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ita_txt, 'tStartRefresh')  # time at next scr refresh
                ita_txt.setAutoDraw(True)
            
            # *ita_kb* updates
            waitOnFlip = False
            if ita_kb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                ita_kb.frameNStart = frameN  # exact frame index
                ita_kb.tStart = t  # local t and not account for scr refresh
                ita_kb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ita_kb, 'tStartRefresh')  # time at next scr refresh
                ita_kb.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ita_kb.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ita_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ita_kb.status == STARTED and not waitOnFlip:
                theseKeys = ita_kb.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
                _ita_kb_allKeys.extend(theseKeys)
                if len(_ita_kb_allKeys):
                    ita_kb.keys = _ita_kb_allKeys[-1].name  # just the last key pressed
                    ita_kb.rt = _ita_kb_allKeys[-1].rt
                    # was this correct?
                    if (ita_kb.keys == str(corrAns)) or (ita_kb.keys == corrAns):
                        ita_kb.corr = 1
                    else:
                        ita_kb.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TRIAL_ITAComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TRIAL_ITA"-------
        for thisComponent in TRIAL_ITAComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("blocco", "ITA")
        thisExp.addData("order", blocco_order)
        ItaLoop.addData('ita_txt.started', ita_txt.tStartRefresh)
        ItaLoop.addData('ita_txt.stopped', ita_txt.tStopRefresh)
        # check responses
        if ita_kb.keys in ['', [], None]:  # No response was made
            ita_kb.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               ita_kb.corr = 1;  # correct non-response
            else:
               ita_kb.corr = 0;  # failed to respond (incorrectly)
        # store data for ItaLoop (TrialHandler)
        ItaLoop.addData('ita_kb.keys',ita_kb.keys)
        ItaLoop.addData('ita_kb.corr', ita_kb.corr)
        if ita_kb.keys != None:  # we had a response
            ItaLoop.addData('ita_kb.rt', ita_kb.rt)
        ItaLoop.addData('ita_kb.started', ita_kb.tStartRefresh)
        ItaLoop.addData('ita_kb.stopped', ita_kb.tStopRefresh)
        # the Routine "TRIAL_ITA" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nb_rep_ita repeats of 'ItaLoop'
    
    # get names of stimulus parameters
    if ItaLoop.trialList in ([], [None], None):
        params = []
    else:
        params = ItaLoop.trialList[0].keys()
    # save data for this loop
    ItaLoop.saveAsExcel(filename + '.xlsx', sheetName='ItaLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    EngLoop = data.TrialHandler(nReps=nb_rep_eng, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condizione.xlsx'),
        seed=None, name='EngLoop')
    thisExp.addLoop(EngLoop)  # add the loop to the experiment
    thisEngLoop = EngLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEngLoop.rgb)
    if thisEngLoop != None:
        for paramName in thisEngLoop:
            exec('{} = thisEngLoop[paramName]'.format(paramName))
    
    for thisEngLoop in EngLoop:
        currentLoop = EngLoop
        # abbreviate parameter names if possible (e.g. rgb = thisEngLoop.rgb)
        if thisEngLoop != None:
            for paramName in thisEngLoop:
                exec('{} = thisEngLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FIXATION"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FIXATIONComponents = [fixation_txt]
        for thisComponent in FIXATIONComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FIXATIONClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FIXATION"-------
        while continueRoutine:
            # get current time
            t = FIXATIONClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FIXATIONClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_txt* updates
            if fixation_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_txt.frameNStart = frameN  # exact frame index
                fixation_txt.tStart = t  # local t and not account for scr refresh
                fixation_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_txt, 'tStartRefresh')  # time at next scr refresh
                fixation_txt.setAutoDraw(True)
            if fixation_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_txt.tStartRefresh + fixation_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_txt.tStop = t  # not accounting for scr refresh
                    fixation_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_txt, 'tStopRefresh')  # time at next scr refresh
                    fixation_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FIXATIONComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FIXATION"-------
        for thisComponent in FIXATIONComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        EngLoop.addData('fixation_txt.started', fixation_txt.tStartRefresh)
        EngLoop.addData('fixation_txt.stopped', fixation_txt.tStopRefresh)
        # the Routine "FIXATION" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "TRIAL_ENG"-------
        continueRoutine = True
        # update component parameters for each repeat
        eng_txt.setColor(colore, colorSpace='rgb')
        eng_txt.setText(word)
        eng_kb.keys = []
        eng_kb.rt = []
        _eng_kb_allKeys = []
        # keep track of which components have finished
        TRIAL_ENGComponents = [eng_txt, eng_kb]
        for thisComponent in TRIAL_ENGComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TRIAL_ENGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TRIAL_ENG"-------
        while continueRoutine:
            # get current time
            t = TRIAL_ENGClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TRIAL_ENGClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *eng_txt* updates
            if eng_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eng_txt.frameNStart = frameN  # exact frame index
                eng_txt.tStart = t  # local t and not account for scr refresh
                eng_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eng_txt, 'tStartRefresh')  # time at next scr refresh
                eng_txt.setAutoDraw(True)
            
            # *eng_kb* updates
            waitOnFlip = False
            if eng_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eng_kb.frameNStart = frameN  # exact frame index
                eng_kb.tStart = t  # local t and not account for scr refresh
                eng_kb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eng_kb, 'tStartRefresh')  # time at next scr refresh
                eng_kb.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(eng_kb.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(eng_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if eng_kb.status == STARTED and not waitOnFlip:
                theseKeys = eng_kb.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
                _eng_kb_allKeys.extend(theseKeys)
                if len(_eng_kb_allKeys):
                    eng_kb.keys = _eng_kb_allKeys[-1].name  # just the last key pressed
                    eng_kb.rt = _eng_kb_allKeys[-1].rt
                    # was this correct?
                    if (eng_kb.keys == str(corrAns)) or (eng_kb.keys == corrAns):
                        eng_kb.corr = 1
                    else:
                        eng_kb.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TRIAL_ENGComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TRIAL_ENG"-------
        for thisComponent in TRIAL_ENGComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("blocco", "ENG")
        thisExp.addData("order", blocco_order)
        
        EngLoop.addData('eng_txt.started', eng_txt.tStartRefresh)
        EngLoop.addData('eng_txt.stopped', eng_txt.tStopRefresh)
        # check responses
        if eng_kb.keys in ['', [], None]:  # No response was made
            eng_kb.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               eng_kb.corr = 1;  # correct non-response
            else:
               eng_kb.corr = 0;  # failed to respond (incorrectly)
        # store data for EngLoop (TrialHandler)
        EngLoop.addData('eng_kb.keys',eng_kb.keys)
        EngLoop.addData('eng_kb.corr', eng_kb.corr)
        if eng_kb.keys != None:  # we had a response
            EngLoop.addData('eng_kb.rt', eng_kb.rt)
        EngLoop.addData('eng_kb.started', eng_kb.tStartRefresh)
        EngLoop.addData('eng_kb.stopped', eng_kb.tStopRefresh)
        # the Routine "TRIAL_ENG" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nb_rep_eng repeats of 'EngLoop'
    
    # get names of stimulus parameters
    if EngLoop.trialList in ([], [None], None):
        params = []
    else:
        params = EngLoop.trialList[0].keys()
    # save data for this loop
    EngLoop.saveAsExcel(filename + '.xlsx', sheetName='EngLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "SWITCH"-------
    continueRoutine = True
    # update component parameters for each repeat
    temp = nb_rep_ita
    nb_rep_ita = nb_rep_eng
    nb_rep_eng = temp
    # keep track of which components have finished
    SWITCHComponents = []
    for thisComponent in SWITCHComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SWITCHClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SWITCH"-------
    while continueRoutine:
        # get current time
        t = SWITCHClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SWITCHClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SWITCHComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SWITCH"-------
    for thisComponent in SWITCHComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "SWITCH" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'ControbilanciamewntoLoop'

# get names of stimulus parameters
if ControbilanciamewntoLoop.trialList in ([], [None], None):
    params = []
else:
    params = ControbilanciamewntoLoop.trialList[0].keys()
# save data for this loop
ControbilanciamewntoLoop.saveAsExcel(filename + '.xlsx', sheetName='ControbilanciamewntoLoop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "LIKERT"-------
continueRoutine = True
# update component parameters for each repeat
likert_sld.reset()
# keep track of which components have finished
LIKERTComponents = [likert_txt, likert_sld, likert_bt]
for thisComponent in LIKERTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LIKERTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LIKERT"-------
while continueRoutine:
    # get current time
    t = LIKERTClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LIKERTClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *likert_txt* updates
    if likert_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        likert_txt.frameNStart = frameN  # exact frame index
        likert_txt.tStart = t  # local t and not account for scr refresh
        likert_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(likert_txt, 'tStartRefresh')  # time at next scr refresh
        likert_txt.setAutoDraw(True)
    
    # *likert_sld* updates
    if likert_sld.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        likert_sld.frameNStart = frameN  # exact frame index
        likert_sld.tStart = t  # local t and not account for scr refresh
        likert_sld.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(likert_sld, 'tStartRefresh')  # time at next scr refresh
        likert_sld.setAutoDraw(True)
    
    # *likert_bt* updates
    if likert_bt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        likert_bt.frameNStart = frameN  # exact frame index
        likert_bt.tStart = t  # local t and not account for scr refresh
        likert_bt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(likert_bt, 'tStartRefresh')  # time at next scr refresh
        likert_bt.setAutoDraw(True)
    if likert_bt.status == STARTED:
        # check whether likert_bt has been pressed
        if likert_bt.isClicked:
            if not likert_bt.wasClicked:
                likert_bt.timesOn.append(likert_bt.buttonClock.getTime()) # store time of first click
                likert_bt.timesOff.append(likert_bt.buttonClock.getTime()) # store time clicked until
            else:
                likert_bt.timesOff[-1] = likert_bt.buttonClock.getTime() # update time clicked until
            if not likert_bt.wasClicked:
                continueRoutine = False  # end routine when likert_bt is clicked
                None
            likert_bt.wasClicked = True  # if likert_bt is still clicked next frame, it is not a new click
        else:
            likert_bt.wasClicked = False  # if likert_bt is clicked next frame, it is a new click
    else:
        likert_bt.wasClicked = False  # if likert_bt is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LIKERTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LIKERT"-------
for thisComponent in LIKERTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('likert_txt.started', likert_txt.tStartRefresh)
thisExp.addData('likert_txt.stopped', likert_txt.tStopRefresh)
thisExp.addData('likert_sld.response', likert_sld.getRating())
thisExp.addData('likert_sld.rt', likert_sld.getRT())
thisExp.addData('likert_sld.started', likert_sld.tStartRefresh)
thisExp.addData('likert_sld.stopped', likert_sld.tStopRefresh)
thisExp.addData('likert_bt.numClicks', likert_bt.numClicks)
if likert_bt.numClicks:
   thisExp.addData('likert_bt.timesOn', likert_bt.timesOn)
   thisExp.addData('likert_bt.timesOff', likert_bt.timesOff)
else:
   thisExp.addData('likert_bt.timesOn', "")
   thisExp.addData('likert_bt.timesOff', "")
# the Routine "LIKERT" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "GRAZIE"-------
continueRoutine = True
# update component parameters for each repeat
grazie_kb.keys = []
grazie_kb.rt = []
_grazie_kb_allKeys = []
# keep track of which components have finished
GRAZIEComponents = [logo_img, grazie_txt, grazie_kb]
for thisComponent in GRAZIEComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GRAZIEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GRAZIE"-------
while continueRoutine:
    # get current time
    t = GRAZIEClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GRAZIEClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *logo_img* updates
    if logo_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        logo_img.frameNStart = frameN  # exact frame index
        logo_img.tStart = t  # local t and not account for scr refresh
        logo_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(logo_img, 'tStartRefresh')  # time at next scr refresh
        logo_img.setAutoDraw(True)
    
    # *grazie_txt* updates
    if grazie_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        grazie_txt.frameNStart = frameN  # exact frame index
        grazie_txt.tStart = t  # local t and not account for scr refresh
        grazie_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grazie_txt, 'tStartRefresh')  # time at next scr refresh
        grazie_txt.setAutoDraw(True)
    
    # *grazie_kb* updates
    if grazie_kb.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        grazie_kb.frameNStart = frameN  # exact frame index
        grazie_kb.tStart = t  # local t and not account for scr refresh
        grazie_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grazie_kb, 'tStartRefresh')  # time at next scr refresh
        grazie_kb.status = STARTED
        # keyboard checking is just starting
        grazie_kb.clock.reset()  # now t=0
        grazie_kb.clearEvents(eventType='keyboard')
    if grazie_kb.status == STARTED:
        theseKeys = grazie_kb.getKeys(keyList=None, waitRelease=False)
        _grazie_kb_allKeys.extend(theseKeys)
        if len(_grazie_kb_allKeys):
            grazie_kb.keys = _grazie_kb_allKeys[-1].name  # just the last key pressed
            grazie_kb.rt = _grazie_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRAZIEComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GRAZIE"-------
for thisComponent in GRAZIEComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "GRAZIE" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='semicolon')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
