#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Tue Apr 18 17:39:56 2023
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
    'gender (m/f)': 'f',
    'participant': '0',
    'ita': '1',
    'eng': '1',
    'pratica': '1',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/thomasquettier/Desktop/stroop_practice/stroop_practice_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
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

# Initialize components for Routine "STIMOLI_ENG"
STIMOLI_ENGClock = core.Clock()
txt_eng = visual.TextStim(win=win, name='txt_eng',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
kb_eng = keyboard.Keyboard()

# Initialize components for Routine "FEEDBACK"
FEEDBACKClock = core.Clock()
count = 0
txt_feedback = visual.TextStim(win=win, name='txt_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "INSTRUCTION"
INSTRUCTIONClock = core.Clock()
txt_instruction = visual.TextStim(win=win, name='txt_instruction',
    text='OK. Ready for the real thing?\n\nRemember, ignore the word itself; press:\nLeft for red LETTERS\nDown for green LETTERS\nRight for blue LETTERS\n(Esc will quit)\n\nPress any key to continue',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
kb_instruction = keyboard.Keyboard()

# Initialize components for Routine "STIMOLI_ENG"
STIMOLI_ENGClock = core.Clock()
txt_eng = visual.TextStim(win=win, name='txt_eng',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
kb_eng = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
txt_isi = visual.TextStim(win=win, name='txt_isi',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PAUSA"
PAUSAClock = core.Clock()
txt_pausa = visual.TextStim(win=win, name='txt_pausa',
    text="Pausa...\n\nPremi 'Spazio' per proseguire",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
kb_pausa = keyboard.Keyboard()

# Initialize components for Routine "ISTRUZIONI"
ISTRUZIONIClock = core.Clock()
txt_istruzioni = visual.TextStim(win=win, name='txt_istruzioni',
    text='\nRicordati, ignora la parola stessa e premi;\nSinistra se vedi lettere ROSSE\nBasso se vedi lettere VERDE\nDestra se vedi lettere BLU\n\n\nPremi qualsiasi tasto per prosseguire',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
kb_istruzioni = keyboard.Keyboard()

# Initialize components for Routine "STIMOLI_ITA"
STIMOLI_ITAClock = core.Clock()
txt_ita = visual.TextStim(win=win, name='txt_ita',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
kb_ita = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
txt_isi = visual.TextStim(win=win, name='txt_isi',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "GRAZIE"
GRAZIEClock = core.Clock()
txt_end = visual.TextStim(win=win, name='txt_end',
    text='Abbiamo finito.\n\nGrazie!',
    font='arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "SETTING"-------
continueRoutine = True
# update component parameters for each repeat
nb_loop_pratica =  int(expInfo["pratica"])
nb_loop_ita =  int(expInfo["ita"])
nb_loop_eng = int(expInfo["eng"])
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
Loop_pratica = data.TrialHandler(nReps=nb_loop_pratica, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='Loop_pratica')
thisExp.addLoop(Loop_pratica)  # add the loop to the experiment
thisLoop_pratica = Loop_pratica.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_pratica.rgb)
if thisLoop_pratica != None:
    for paramName in thisLoop_pratica:
        exec('{} = thisLoop_pratica[paramName]'.format(paramName))

for thisLoop_pratica in Loop_pratica:
    currentLoop = Loop_pratica
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_pratica.rgb)
    if thisLoop_pratica != None:
        for paramName in thisLoop_pratica:
            exec('{} = thisLoop_pratica[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "STIMOLI_ENG"-------
    continueRoutine = True
    # update component parameters for each repeat
    txt_eng.setColor(letterColor, colorSpace='rgb')
    txt_eng.setText(word)
    kb_eng.keys = []
    kb_eng.rt = []
    _kb_eng_allKeys = []
    # keep track of which components have finished
    STIMOLI_ENGComponents = [txt_eng, kb_eng]
    for thisComponent in STIMOLI_ENGComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    STIMOLI_ENGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "STIMOLI_ENG"-------
    while continueRoutine:
        # get current time
        t = STIMOLI_ENGClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=STIMOLI_ENGClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_eng* updates
        if txt_eng.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            txt_eng.frameNStart = frameN  # exact frame index
            txt_eng.tStart = t  # local t and not account for scr refresh
            txt_eng.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_eng, 'tStartRefresh')  # time at next scr refresh
            txt_eng.setAutoDraw(True)
        
        # *kb_eng* updates
        waitOnFlip = False
        if kb_eng.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            kb_eng.frameNStart = frameN  # exact frame index
            kb_eng.tStart = t  # local t and not account for scr refresh
            kb_eng.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(kb_eng, 'tStartRefresh')  # time at next scr refresh
            kb_eng.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(kb_eng.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(kb_eng.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if kb_eng.status == STARTED and not waitOnFlip:
            theseKeys = kb_eng.getKeys(keyList=["left","down","right"], waitRelease=False)
            _kb_eng_allKeys.extend(theseKeys)
            if len(_kb_eng_allKeys):
                kb_eng.keys = _kb_eng_allKeys[-1].name  # just the last key pressed
                kb_eng.rt = _kb_eng_allKeys[-1].rt
                # was this correct?
                if (kb_eng.keys == str(corrAns)) or (kb_eng.keys == corrAns):
                    kb_eng.corr = 1
                else:
                    kb_eng.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in STIMOLI_ENGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "STIMOLI_ENG"-------
    for thisComponent in STIMOLI_ENGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_pratica.addData('txt_eng.started', txt_eng.tStartRefresh)
    Loop_pratica.addData('txt_eng.stopped', txt_eng.tStopRefresh)
    # check responses
    if kb_eng.keys in ['', [], None]:  # No response was made
        kb_eng.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           kb_eng.corr = 1;  # correct non-response
        else:
           kb_eng.corr = 0;  # failed to respond (incorrectly)
    # store data for Loop_pratica (TrialHandler)
    Loop_pratica.addData('kb_eng.keys',kb_eng.keys)
    Loop_pratica.addData('kb_eng.corr', kb_eng.corr)
    if kb_eng.keys != None:  # we had a response
        Loop_pratica.addData('kb_eng.rt', kb_eng.rt)
    Loop_pratica.addData('kb_eng.started', kb_eng.tStartRefresh)
    Loop_pratica.addData('kb_eng.stopped', kb_eng.tStopRefresh)
    # the Routine "STIMOLI_ENG" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "FEEDBACK"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    if kb_eng.corr:
        count = count+1
        msg = "Correct! RT={:.3f}".format(kb_eng.rt)
    else:
        msg = "Oops! That was wrong"
        count = 0
    txt_feedback.setText(msg)
    # keep track of which components have finished
    FEEDBACKComponents = [txt_feedback]
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
        
        # *txt_feedback* updates
        if txt_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_feedback.frameNStart = frameN  # exact frame index
            txt_feedback.tStart = t  # local t and not account for scr refresh
            txt_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_feedback, 'tStartRefresh')  # time at next scr refresh
            txt_feedback.setAutoDraw(True)
        if txt_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > txt_feedback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                txt_feedback.tStop = t  # not accounting for scr refresh
                txt_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(txt_feedback, 'tStopRefresh')  # time at next scr refresh
                txt_feedback.setAutoDraw(False)
        
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
    if count == 5:
            Loop_pratica.finished=True
            continueRoutine = False
    Loop_pratica.addData('txt_feedback.started', txt_feedback.tStartRefresh)
    Loop_pratica.addData('txt_feedback.stopped', txt_feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed nb_loop_pratica repeats of 'Loop_pratica'


# ------Prepare to start Routine "INSTRUCTION"-------
continueRoutine = True
# update component parameters for each repeat
kb_instruction.keys = []
kb_instruction.rt = []
_kb_instruction_allKeys = []
# keep track of which components have finished
INSTRUCTIONComponents = [txt_instruction, kb_instruction]
for thisComponent in INSTRUCTIONComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
INSTRUCTIONClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "INSTRUCTION"-------
while continueRoutine:
    # get current time
    t = INSTRUCTIONClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=INSTRUCTIONClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_instruction* updates
    if txt_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        txt_instruction.frameNStart = frameN  # exact frame index
        txt_instruction.tStart = t  # local t and not account for scr refresh
        txt_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_instruction, 'tStartRefresh')  # time at next scr refresh
        txt_instruction.setAutoDraw(True)
    
    # *kb_instruction* updates
    waitOnFlip = False
    if kb_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        kb_instruction.frameNStart = frameN  # exact frame index
        kb_instruction.tStart = t  # local t and not account for scr refresh
        kb_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(kb_instruction, 'tStartRefresh')  # time at next scr refresh
        kb_instruction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(kb_instruction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(kb_instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if kb_instruction.status == STARTED and not waitOnFlip:
        theseKeys = kb_instruction.getKeys(keyList=None, waitRelease=False)
        _kb_instruction_allKeys.extend(theseKeys)
        if len(_kb_instruction_allKeys):
            kb_instruction.keys = _kb_instruction_allKeys[-1].name  # just the last key pressed
            kb_instruction.rt = _kb_instruction_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in INSTRUCTIONComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "INSTRUCTION"-------
for thisComponent in INSTRUCTIONComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_instruction.started', txt_instruction.tStartRefresh)
thisExp.addData('txt_instruction.stopped', txt_instruction.tStopRefresh)
# the Routine "INSTRUCTION" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop_eng = data.TrialHandler(nReps=nb_loop_eng, method='random', 
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
    
    # ------Prepare to start Routine "STIMOLI_ENG"-------
    continueRoutine = True
    # update component parameters for each repeat
    txt_eng.setColor(letterColor, colorSpace='rgb')
    txt_eng.setText(word)
    kb_eng.keys = []
    kb_eng.rt = []
    _kb_eng_allKeys = []
    # keep track of which components have finished
    STIMOLI_ENGComponents = [txt_eng, kb_eng]
    for thisComponent in STIMOLI_ENGComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    STIMOLI_ENGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "STIMOLI_ENG"-------
    while continueRoutine:
        # get current time
        t = STIMOLI_ENGClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=STIMOLI_ENGClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_eng* updates
        if txt_eng.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            txt_eng.frameNStart = frameN  # exact frame index
            txt_eng.tStart = t  # local t and not account for scr refresh
            txt_eng.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_eng, 'tStartRefresh')  # time at next scr refresh
            txt_eng.setAutoDraw(True)
        
        # *kb_eng* updates
        waitOnFlip = False
        if kb_eng.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            kb_eng.frameNStart = frameN  # exact frame index
            kb_eng.tStart = t  # local t and not account for scr refresh
            kb_eng.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(kb_eng, 'tStartRefresh')  # time at next scr refresh
            kb_eng.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(kb_eng.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(kb_eng.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if kb_eng.status == STARTED and not waitOnFlip:
            theseKeys = kb_eng.getKeys(keyList=["left","down","right"], waitRelease=False)
            _kb_eng_allKeys.extend(theseKeys)
            if len(_kb_eng_allKeys):
                kb_eng.keys = _kb_eng_allKeys[-1].name  # just the last key pressed
                kb_eng.rt = _kb_eng_allKeys[-1].rt
                # was this correct?
                if (kb_eng.keys == str(corrAns)) or (kb_eng.keys == corrAns):
                    kb_eng.corr = 1
                else:
                    kb_eng.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in STIMOLI_ENGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "STIMOLI_ENG"-------
    for thisComponent in STIMOLI_ENGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_eng.addData('txt_eng.started', txt_eng.tStartRefresh)
    Loop_eng.addData('txt_eng.stopped', txt_eng.tStopRefresh)
    # check responses
    if kb_eng.keys in ['', [], None]:  # No response was made
        kb_eng.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           kb_eng.corr = 1;  # correct non-response
        else:
           kb_eng.corr = 0;  # failed to respond (incorrectly)
    # store data for Loop_eng (TrialHandler)
    Loop_eng.addData('kb_eng.keys',kb_eng.keys)
    Loop_eng.addData('kb_eng.corr', kb_eng.corr)
    if kb_eng.keys != None:  # we had a response
        Loop_eng.addData('kb_eng.rt', kb_eng.rt)
    Loop_eng.addData('kb_eng.started', kb_eng.tStartRefresh)
    Loop_eng.addData('kb_eng.stopped', kb_eng.tStopRefresh)
    # the Routine "STIMOLI_ENG" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [txt_isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_isi* updates
        if txt_isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_isi.frameNStart = frameN  # exact frame index
            txt_isi.tStart = t  # local t and not account for scr refresh
            txt_isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_isi, 'tStartRefresh')  # time at next scr refresh
            txt_isi.setAutoDraw(True)
        if txt_isi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > txt_isi.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                txt_isi.tStop = t  # not accounting for scr refresh
                txt_isi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(txt_isi, 'tStopRefresh')  # time at next scr refresh
                txt_isi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_eng.addData('txt_isi.started', txt_isi.tStartRefresh)
    Loop_eng.addData('txt_isi.stopped', txt_isi.tStopRefresh)
    thisExp.nextEntry()
    
# completed nb_loop_eng repeats of 'Loop_eng'


# ------Prepare to start Routine "PAUSA"-------
continueRoutine = True
# update component parameters for each repeat
kb_pausa.keys = []
kb_pausa.rt = []
_kb_pausa_allKeys = []
# keep track of which components have finished
PAUSAComponents = [txt_pausa, kb_pausa]
for thisComponent in PAUSAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PAUSAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PAUSA"-------
while continueRoutine:
    # get current time
    t = PAUSAClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PAUSAClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_pausa* updates
    if txt_pausa.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        txt_pausa.frameNStart = frameN  # exact frame index
        txt_pausa.tStart = t  # local t and not account for scr refresh
        txt_pausa.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_pausa, 'tStartRefresh')  # time at next scr refresh
        txt_pausa.setAutoDraw(True)
    
    # *kb_pausa* updates
    waitOnFlip = False
    if kb_pausa.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        kb_pausa.frameNStart = frameN  # exact frame index
        kb_pausa.tStart = t  # local t and not account for scr refresh
        kb_pausa.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(kb_pausa, 'tStartRefresh')  # time at next scr refresh
        kb_pausa.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(kb_pausa.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(kb_pausa.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if kb_pausa.status == STARTED and not waitOnFlip:
        theseKeys = kb_pausa.getKeys(keyList=None, waitRelease=False)
        _kb_pausa_allKeys.extend(theseKeys)
        if len(_kb_pausa_allKeys):
            kb_pausa.keys = _kb_pausa_allKeys[-1].name  # just the last key pressed
            kb_pausa.rt = _kb_pausa_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PAUSAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PAUSA"-------
for thisComponent in PAUSAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_pausa.started', txt_pausa.tStartRefresh)
thisExp.addData('txt_pausa.stopped', txt_pausa.tStopRefresh)
# the Routine "PAUSA" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISTRUZIONI"-------
continueRoutine = True
# update component parameters for each repeat
kb_istruzioni.keys = []
kb_istruzioni.rt = []
_kb_istruzioni_allKeys = []
# keep track of which components have finished
ISTRUZIONIComponents = [txt_istruzioni, kb_istruzioni]
for thisComponent in ISTRUZIONIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISTRUZIONIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISTRUZIONI"-------
while continueRoutine:
    # get current time
    t = ISTRUZIONIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISTRUZIONIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_istruzioni* updates
    if txt_istruzioni.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        txt_istruzioni.frameNStart = frameN  # exact frame index
        txt_istruzioni.tStart = t  # local t and not account for scr refresh
        txt_istruzioni.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_istruzioni, 'tStartRefresh')  # time at next scr refresh
        txt_istruzioni.setAutoDraw(True)
    
    # *kb_istruzioni* updates
    waitOnFlip = False
    if kb_istruzioni.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        kb_istruzioni.frameNStart = frameN  # exact frame index
        kb_istruzioni.tStart = t  # local t and not account for scr refresh
        kb_istruzioni.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(kb_istruzioni, 'tStartRefresh')  # time at next scr refresh
        kb_istruzioni.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(kb_istruzioni.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(kb_istruzioni.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if kb_istruzioni.status == STARTED and not waitOnFlip:
        theseKeys = kb_istruzioni.getKeys(keyList=None, waitRelease=False)
        _kb_istruzioni_allKeys.extend(theseKeys)
        if len(_kb_istruzioni_allKeys):
            kb_istruzioni.keys = _kb_istruzioni_allKeys[-1].name  # just the last key pressed
            kb_istruzioni.rt = _kb_istruzioni_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISTRUZIONIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISTRUZIONI"-------
for thisComponent in ISTRUZIONIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_istruzioni.started', txt_istruzioni.tStartRefresh)
thisExp.addData('txt_istruzioni.stopped', txt_istruzioni.tStopRefresh)
# the Routine "ISTRUZIONI" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop_ita = data.TrialHandler(nReps=nb_loop_ita, method='random', 
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
    
    # ------Prepare to start Routine "STIMOLI_ITA"-------
    continueRoutine = True
    # update component parameters for each repeat
    txt_ita.setColor(letterColor, colorSpace='rgb')
    txt_ita.setText(parola)
    kb_ita.keys = []
    kb_ita.rt = []
    _kb_ita_allKeys = []
    # keep track of which components have finished
    STIMOLI_ITAComponents = [txt_ita, kb_ita]
    for thisComponent in STIMOLI_ITAComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    STIMOLI_ITAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "STIMOLI_ITA"-------
    while continueRoutine:
        # get current time
        t = STIMOLI_ITAClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=STIMOLI_ITAClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_ita* updates
        if txt_ita.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            txt_ita.frameNStart = frameN  # exact frame index
            txt_ita.tStart = t  # local t and not account for scr refresh
            txt_ita.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_ita, 'tStartRefresh')  # time at next scr refresh
            txt_ita.setAutoDraw(True)
        
        # *kb_ita* updates
        waitOnFlip = False
        if kb_ita.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            kb_ita.frameNStart = frameN  # exact frame index
            kb_ita.tStart = t  # local t and not account for scr refresh
            kb_ita.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(kb_ita, 'tStartRefresh')  # time at next scr refresh
            kb_ita.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(kb_ita.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(kb_ita.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if kb_ita.status == STARTED and not waitOnFlip:
            theseKeys = kb_ita.getKeys(keyList=["left","down","right"], waitRelease=False)
            _kb_ita_allKeys.extend(theseKeys)
            if len(_kb_ita_allKeys):
                kb_ita.keys = _kb_ita_allKeys[-1].name  # just the last key pressed
                kb_ita.rt = _kb_ita_allKeys[-1].rt
                # was this correct?
                if (kb_ita.keys == str(corrAns)) or (kb_ita.keys == corrAns):
                    kb_ita.corr = 1
                else:
                    kb_ita.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in STIMOLI_ITAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "STIMOLI_ITA"-------
    for thisComponent in STIMOLI_ITAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_ita.addData('txt_ita.started', txt_ita.tStartRefresh)
    Loop_ita.addData('txt_ita.stopped', txt_ita.tStopRefresh)
    # check responses
    if kb_ita.keys in ['', [], None]:  # No response was made
        kb_ita.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           kb_ita.corr = 1;  # correct non-response
        else:
           kb_ita.corr = 0;  # failed to respond (incorrectly)
    # store data for Loop_ita (TrialHandler)
    Loop_ita.addData('kb_ita.keys',kb_ita.keys)
    Loop_ita.addData('kb_ita.corr', kb_ita.corr)
    if kb_ita.keys != None:  # we had a response
        Loop_ita.addData('kb_ita.rt', kb_ita.rt)
    Loop_ita.addData('kb_ita.started', kb_ita.tStartRefresh)
    Loop_ita.addData('kb_ita.stopped', kb_ita.tStopRefresh)
    # the Routine "STIMOLI_ITA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [txt_isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_isi* updates
        if txt_isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_isi.frameNStart = frameN  # exact frame index
            txt_isi.tStart = t  # local t and not account for scr refresh
            txt_isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_isi, 'tStartRefresh')  # time at next scr refresh
            txt_isi.setAutoDraw(True)
        if txt_isi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > txt_isi.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                txt_isi.tStop = t  # not accounting for scr refresh
                txt_isi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(txt_isi, 'tStopRefresh')  # time at next scr refresh
                txt_isi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_ita.addData('txt_isi.started', txt_isi.tStartRefresh)
    Loop_ita.addData('txt_isi.stopped', txt_isi.tStopRefresh)
    thisExp.nextEntry()
    
# completed nb_loop_ita repeats of 'Loop_ita'


# ------Prepare to start Routine "GRAZIE"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
GRAZIEComponents = [txt_end]
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
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GRAZIEClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GRAZIEClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_end* updates
    if txt_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_end.frameNStart = frameN  # exact frame index
        txt_end.tStart = t  # local t and not account for scr refresh
        txt_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_end, 'tStartRefresh')  # time at next scr refresh
        txt_end.setAutoDraw(True)
    if txt_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt_end.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            txt_end.tStop = t  # not accounting for scr refresh
            txt_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt_end, 'tStopRefresh')  # time at next scr refresh
            txt_end.setAutoDraw(False)
    
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
thisExp.addData('txt_end.started', txt_end.tStartRefresh)
thisExp.addData('txt_end.stopped', txt_end.tStopRefresh)

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
