#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Wed Oct 18 07:58:51 2023
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
expName = 'stroopeng'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'n_rep': '2',
    'session': '001',
    'Gender': '',
    'ENG level': 'B1',
    'ITA level': 'B1',
    'lingua': 'ITA',
    'rep': '3',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/thomasquettier/Desktop/ARCAPY/stroop multilingual/stroopeng.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
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

# Initialize components for Routine "FLAG"
FLAGClock = core.Clock()
  loop_ita = 0
  loop_eng = 0
ita_img = visual.Rect(
    win=win, name='ita_img',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(-0.5, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='green',
    opacity=None, depth=-1.0, interpolate=True)
eng_img = visual.Rect(
    win=win, name='eng_img',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0.5, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='blue',
    opacity=None, depth=-2.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "ISTR"
ISTRClock = core.Clock()
istr_txt = visual.TextStim(win=win, name='istr_txt',
    text='\nRemember, ignore the word itself; press:\nLeft for red LETTERS\nDown for green LETTERS\nRight for blue LETTERS\n(Esc will quit)\n\nPress “space” to continue',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
istr_kb = keyboard.Keyboard()

# Initialize components for Routine "BLOCCO_ENG"
BLOCCO_ENGClock = core.Clock()
eng_txt = visual.TextStim(win=win, name='eng_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
eng_kb = keyboard.Keyboard()

# Initialize components for Routine "BlOCCO_ITA"
BlOCCO_ITAClock = core.Clock()
ita_txt = visual.TextStim(win=win, name='ita_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ita_kb = keyboard.Keyboard()

# Initialize components for Routine "GRAZIE"
GRAZIEClock = core.Clock()
grazie_txt = visual.TextStim(win=win, name='grazie_txt',
    text='This is the end of the experiment.\n\nThanks!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
grazie_kb = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "FLAG"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
FLAGComponents = [ita_img, eng_img, mouse]
for thisComponent in FLAGComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FLAGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FLAG"-------
while continueRoutine:
    # get current time
    t = FLAGClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FLAGClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ita_img* updates
    if ita_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ita_img.frameNStart = frameN  # exact frame index
        ita_img.tStart = t  # local t and not account for scr refresh
        ita_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ita_img, 'tStartRefresh')  # time at next scr refresh
        ita_img.setAutoDraw(True)
    
    # *eng_img* updates
    if eng_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eng_img.frameNStart = frameN  # exact frame index
        eng_img.tStart = t  # local t and not account for scr refresh
        eng_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eng_img, 'tStartRefresh')  # time at next scr refresh
        eng_img.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([ita_img, eng_img])
                    clickableList = [ita_img, eng_img]
                except:
                    clickableList = [[ita_img, eng_img]]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FLAGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FLAG"-------
for thisComponent in FLAGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


if mouse.clicked_name[0] == 'ita_img':
  loop_ita = expInfo['n_rep']
  loop_eng = 0
else:
   loop_ita = 0
   loop_eng = expInfo['n_rep']
thisExp.addData('ita_img.started', ita_img.tStartRefresh)
thisExp.addData('ita_img.stopped', ita_img.tStopRefresh)
thisExp.addData('eng_img.started', eng_img.tStartRefresh)
thisExp.addData('eng_img.stopped', eng_img.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.clicked_name', mouse.clicked_name)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "FLAG" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISTR"-------
continueRoutine = True
# update component parameters for each repeat
istr_kb.keys = []
istr_kb.rt = []
_istr_kb_allKeys = []
# keep track of which components have finished
ISTRComponents = [istr_txt, istr_kb]
for thisComponent in ISTRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISTRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISTR"-------
while continueRoutine:
    # get current time
    t = ISTRClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISTRClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *istr_txt* updates
    if istr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        istr_txt.frameNStart = frameN  # exact frame index
        istr_txt.tStart = t  # local t and not account for scr refresh
        istr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(istr_txt, 'tStartRefresh')  # time at next scr refresh
        istr_txt.setAutoDraw(True)
    
    # *istr_kb* updates
    waitOnFlip = False
    if istr_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        istr_kb.frameNStart = frameN  # exact frame index
        istr_kb.tStart = t  # local t and not account for scr refresh
        istr_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(istr_kb, 'tStartRefresh')  # time at next scr refresh
        istr_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(istr_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(istr_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if istr_kb.status == STARTED and not waitOnFlip:
        theseKeys = istr_kb.getKeys(keyList=['space'], waitRelease=False)
        _istr_kb_allKeys.extend(theseKeys)
        if len(_istr_kb_allKeys):
            istr_kb.keys = _istr_kb_allKeys[-1].name  # just the last key pressed
            istr_kb.rt = _istr_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISTRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISTR"-------
for thisComponent in ISTRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('istr_txt.started', istr_txt.tStartRefresh)
thisExp.addData('istr_txt.stopped', istr_txt.tStopRefresh)
# check responses
if istr_kb.keys in ['', [], None]:  # No response was made
    istr_kb.keys = None
thisExp.addData('istr_kb.keys',istr_kb.keys)
if istr_kb.keys != None:  # we had a response
    thisExp.addData('istr_kb.rt', istr_kb.rt)
thisExp.nextEntry()
# the Routine "ISTR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop_eng = data.TrialHandler(nReps=loop_eng, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='Loop_eng')
thisExp.addLoop(Loop_eng)  # add the loop to the experiment
thisLoop_eng = Loop_eng.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_eng.rgb)
if thisLoop_eng != None:
    for paramName in thisLoop_eng:
        exec('{} = thisLoop_eng[paramName]'.format(paramName))

for thisLoop_eng in Loop_eng:
    currentLoop = Loop_eng
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_eng.rgb)
    if thisLoop_eng != None:
        for paramName in thisLoop_eng:
            exec('{} = thisLoop_eng[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BLOCCO_ENG"-------
    continueRoutine = True
    # update component parameters for each repeat
    eng_txt.setColor(letterColor, colorSpace='rgb')
    eng_txt.setText(word)
    eng_kb.keys = []
    eng_kb.rt = []
    _eng_kb_allKeys = []
    # keep track of which components have finished
    BLOCCO_ENGComponents = [eng_txt, eng_kb]
    for thisComponent in BLOCCO_ENGComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BLOCCO_ENGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BLOCCO_ENG"-------
    while continueRoutine:
        # get current time
        t = BLOCCO_ENGClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BLOCCO_ENGClock)
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
            theseKeys = eng_kb.getKeys(keyList=['left','right','down'], waitRelease=False)
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
        for thisComponent in BLOCCO_ENGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BLOCCO_ENG"-------
    for thisComponent in BLOCCO_ENGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_eng.addData('eng_txt.started', eng_txt.tStartRefresh)
    Loop_eng.addData('eng_txt.stopped', eng_txt.tStopRefresh)
    # check responses
    if eng_kb.keys in ['', [], None]:  # No response was made
        eng_kb.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           eng_kb.corr = 1;  # correct non-response
        else:
           eng_kb.corr = 0;  # failed to respond (incorrectly)
    # store data for Loop_eng (TrialHandler)
    Loop_eng.addData('eng_kb.keys',eng_kb.keys)
    Loop_eng.addData('eng_kb.corr', eng_kb.corr)
    if eng_kb.keys != None:  # we had a response
        Loop_eng.addData('eng_kb.rt', eng_kb.rt)
    Loop_eng.addData('eng_kb.started', eng_kb.tStartRefresh)
    Loop_eng.addData('eng_kb.stopped', eng_kb.tStopRefresh)
    # the Routine "BLOCCO_ENG" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed loop_eng repeats of 'Loop_eng'


# set up handler to look after randomisation of conditions etc
Loop_ita = data.TrialHandler(nReps=loop_ita, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='Loop_ita')
thisExp.addLoop(Loop_ita)  # add the loop to the experiment
thisLoop_ita = Loop_ita.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_ita.rgb)
if thisLoop_ita != None:
    for paramName in thisLoop_ita:
        exec('{} = thisLoop_ita[paramName]'.format(paramName))

for thisLoop_ita in Loop_ita:
    currentLoop = Loop_ita
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_ita.rgb)
    if thisLoop_ita != None:
        for paramName in thisLoop_ita:
            exec('{} = thisLoop_ita[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BlOCCO_ITA"-------
    continueRoutine = True
    # update component parameters for each repeat
    ita_txt.setColor(letterColor, colorSpace='rgb')
    ita_txt.setText(parola)
    ita_kb.keys = []
    ita_kb.rt = []
    _ita_kb_allKeys = []
    # keep track of which components have finished
    BlOCCO_ITAComponents = [ita_txt, ita_kb]
    for thisComponent in BlOCCO_ITAComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlOCCO_ITAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlOCCO_ITA"-------
    while continueRoutine:
        # get current time
        t = BlOCCO_ITAClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlOCCO_ITAClock)
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
            theseKeys = ita_kb.getKeys(keyList=['left','right','down'], waitRelease=False)
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
        for thisComponent in BlOCCO_ITAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlOCCO_ITA"-------
    for thisComponent in BlOCCO_ITAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_ita.addData('ita_txt.started', ita_txt.tStartRefresh)
    Loop_ita.addData('ita_txt.stopped', ita_txt.tStopRefresh)
    # check responses
    if ita_kb.keys in ['', [], None]:  # No response was made
        ita_kb.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           ita_kb.corr = 1;  # correct non-response
        else:
           ita_kb.corr = 0;  # failed to respond (incorrectly)
    # store data for Loop_ita (TrialHandler)
    Loop_ita.addData('ita_kb.keys',ita_kb.keys)
    Loop_ita.addData('ita_kb.corr', ita_kb.corr)
    if ita_kb.keys != None:  # we had a response
        Loop_ita.addData('ita_kb.rt', ita_kb.rt)
    Loop_ita.addData('ita_kb.started', ita_kb.tStartRefresh)
    Loop_ita.addData('ita_kb.stopped', ita_kb.tStopRefresh)
    # the Routine "BlOCCO_ITA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed loop_ita repeats of 'Loop_ita'


# ------Prepare to start Routine "GRAZIE"-------
continueRoutine = True
# update component parameters for each repeat
grazie_kb.keys = []
grazie_kb.rt = []
_grazie_kb_allKeys = []
# keep track of which components have finished
GRAZIEComponents = [grazie_txt, grazie_kb]
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
    
    # *grazie_txt* updates
    if grazie_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        grazie_txt.frameNStart = frameN  # exact frame index
        grazie_txt.tStart = t  # local t and not account for scr refresh
        grazie_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grazie_txt, 'tStartRefresh')  # time at next scr refresh
        grazie_txt.setAutoDraw(True)
    
    # *grazie_kb* updates
    waitOnFlip = False
    if grazie_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        grazie_kb.frameNStart = frameN  # exact frame index
        grazie_kb.tStart = t  # local t and not account for scr refresh
        grazie_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grazie_kb, 'tStartRefresh')  # time at next scr refresh
        grazie_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(grazie_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(grazie_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if grazie_kb.status == STARTED and not waitOnFlip:
        theseKeys = grazie_kb.getKeys(keyList=['space'], waitRelease=False)
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
thisExp.addData('grazie_txt.started', grazie_txt.tStartRefresh)
thisExp.addData('grazie_txt.stopped', grazie_txt.tStopRefresh)
# check responses
if grazie_kb.keys in ['', [], None]:  # No response was made
    grazie_kb.keys = None
thisExp.addData('grazie_kb.keys',grazie_kb.keys)
if grazie_kb.keys != None:  # we had a response
    thisExp.addData('grazie_kb.rt', grazie_kb.rt)
thisExp.addData('grazie_kb.started', grazie_kb.tStartRefresh)
thisExp.addData('grazie_kb.stopped', grazie_kb.tStopRefresh)
thisExp.nextEntry()
# the Routine "GRAZIE" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
