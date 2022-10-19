#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Wed Oct 19 08:01:56 2022
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
    'practice': '1',
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
    originPath='/Users/thomasquettier/Desktop/stroop_practice/stroop_lastrun.py',
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
# initialisation di variabili 

msg = '' # per FEEDBACK

practice = expInfo['practice'] # per nb rep PracticeLoop

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
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TRIAL"
TRIALClock = core.Clock()
word_txt = visual.TextStim(win=win, name='word_txt',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
resp_kb = keyboard.Keyboard()

# Initialize components for Routine "FEEDBACK"
FEEDBACKClock = core.Clock()
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
    text="Ottimo, hai finito la prova,\n\nAdesso iniziamo l'esperimento, ricordati di premere:\nSINISTRA se il colore è ROSSO\nBASSO se il colore è VERDE\nDESTRA se il colore è BLU\n\n\nPremi qualsiasi tasto per iniziare",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
istr_esperimento_kb = keyboard.Keyboard()

# Initialize components for Routine "FIXATION"
FIXATIONClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TRIAL"
TRIALClock = core.Clock()
word_txt = visual.TextStim(win=win, name='word_txt',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
resp_kb = keyboard.Keyboard()

# Initialize components for Routine "GRAZIE"
GRAZIEClock = core.Clock()
grazie_txt = visual.TextStim(win=win, name='grazie_txt',
    text="L'esperimento è finito.\n\nGrazie!",
    font='arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
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
PracticeLoop = data.TrialHandler(nReps=practice, method='random', 
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
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FIXATIONComponents = [text]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FIXATIONClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FIXATIONClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
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
    PracticeLoop.addData('text.started', text.tStartRefresh)
    PracticeLoop.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "TRIAL"-------
    continueRoutine = True
    # update component parameters for each repeat
    word_txt.setColor(colore, colorSpace='rgb')
    word_txt.setText(parola)
    resp_kb.keys = []
    resp_kb.rt = []
    _resp_kb_allKeys = []
    # keep track of which components have finished
    TRIALComponents = [word_txt, resp_kb]
    for thisComponent in TRIALComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TRIALClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TRIAL"-------
    while continueRoutine:
        # get current time
        t = TRIALClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TRIALClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word_txt* updates
        if word_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            word_txt.frameNStart = frameN  # exact frame index
            word_txt.tStart = t  # local t and not account for scr refresh
            word_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_txt, 'tStartRefresh')  # time at next scr refresh
            word_txt.setAutoDraw(True)
        
        # *resp_kb* updates
        waitOnFlip = False
        if resp_kb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            resp_kb.frameNStart = frameN  # exact frame index
            resp_kb.tStart = t  # local t and not account for scr refresh
            resp_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_kb, 'tStartRefresh')  # time at next scr refresh
            resp_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_kb.status == STARTED and not waitOnFlip:
            theseKeys = resp_kb.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
            _resp_kb_allKeys.extend(theseKeys)
            if len(_resp_kb_allKeys):
                resp_kb.keys = _resp_kb_allKeys[-1].name  # just the last key pressed
                resp_kb.rt = _resp_kb_allKeys[-1].rt
                # was this correct?
                if (resp_kb.keys == str(corrAns)) or (resp_kb.keys == corrAns):
                    resp_kb.corr = 1
                else:
                    resp_kb.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TRIALComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TRIAL"-------
    for thisComponent in TRIALComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeLoop.addData('word_txt.started', word_txt.tStartRefresh)
    PracticeLoop.addData('word_txt.stopped', word_txt.tStopRefresh)
    # check responses
    if resp_kb.keys in ['', [], None]:  # No response was made
        resp_kb.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp_kb.corr = 1;  # correct non-response
        else:
           resp_kb.corr = 0;  # failed to respond (incorrectly)
    # store data for PracticeLoop (TrialHandler)
    PracticeLoop.addData('resp_kb.keys',resp_kb.keys)
    PracticeLoop.addData('resp_kb.corr', resp_kb.corr)
    if resp_kb.keys != None:  # we had a response
        PracticeLoop.addData('resp_kb.rt', resp_kb.rt)
    PracticeLoop.addData('resp_kb.started', resp_kb.tStartRefresh)
    PracticeLoop.addData('resp_kb.stopped', resp_kb.tStopRefresh)
    # the Routine "TRIAL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "FEEDBACK"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # "resp_kb.corr" è ottenuto se trial 
    # routine  "resp_kb" registra la risposta correta
    
    if resp_kb.corr: 
      msg="Bravo! RT=%.3f" %(resp_kb.rt)
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
    thisExp.nextEntry()
    
# completed practice repeats of 'PracticeLoop'

# get names of stimulus parameters
if PracticeLoop.trialList in ([], [None], None):
    params = []
else:
    params = PracticeLoop.trialList[0].keys()
# save data for this loop
PracticeLoop.saveAsExcel(filename + '.xlsx', sheetName='PracticeLoop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
trials = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condizione.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FIXATION"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FIXATIONComponents = [text]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FIXATIONClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FIXATIONClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
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
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "TRIAL"-------
    continueRoutine = True
    # update component parameters for each repeat
    word_txt.setColor(colore, colorSpace='rgb')
    word_txt.setText(parola)
    resp_kb.keys = []
    resp_kb.rt = []
    _resp_kb_allKeys = []
    # keep track of which components have finished
    TRIALComponents = [word_txt, resp_kb]
    for thisComponent in TRIALComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TRIALClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TRIAL"-------
    while continueRoutine:
        # get current time
        t = TRIALClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TRIALClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word_txt* updates
        if word_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            word_txt.frameNStart = frameN  # exact frame index
            word_txt.tStart = t  # local t and not account for scr refresh
            word_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_txt, 'tStartRefresh')  # time at next scr refresh
            word_txt.setAutoDraw(True)
        
        # *resp_kb* updates
        waitOnFlip = False
        if resp_kb.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            resp_kb.frameNStart = frameN  # exact frame index
            resp_kb.tStart = t  # local t and not account for scr refresh
            resp_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_kb, 'tStartRefresh')  # time at next scr refresh
            resp_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_kb.status == STARTED and not waitOnFlip:
            theseKeys = resp_kb.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
            _resp_kb_allKeys.extend(theseKeys)
            if len(_resp_kb_allKeys):
                resp_kb.keys = _resp_kb_allKeys[-1].name  # just the last key pressed
                resp_kb.rt = _resp_kb_allKeys[-1].rt
                # was this correct?
                if (resp_kb.keys == str(corrAns)) or (resp_kb.keys == corrAns):
                    resp_kb.corr = 1
                else:
                    resp_kb.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TRIALComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TRIAL"-------
    for thisComponent in TRIALComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('word_txt.started', word_txt.tStartRefresh)
    trials.addData('word_txt.stopped', word_txt.tStopRefresh)
    # check responses
    if resp_kb.keys in ['', [], None]:  # No response was made
        resp_kb.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp_kb.corr = 1;  # correct non-response
        else:
           resp_kb.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp_kb.keys',resp_kb.keys)
    trials.addData('resp_kb.corr', resp_kb.corr)
    if resp_kb.keys != None:  # we had a response
        trials.addData('resp_kb.rt', resp_kb.rt)
    trials.addData('resp_kb.started', resp_kb.tStartRefresh)
    trials.addData('resp_kb.stopped', resp_kb.tStopRefresh)
    # the Routine "TRIAL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
