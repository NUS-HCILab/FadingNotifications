#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Thu 11 Nov 2021 09:53:18 AM +08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import participant_config
import  trigger_notification
import stimuli_generation
import reading_passages
import  device_driver
import  log_utility



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'tasks_psychopy'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s/%s_%s_%s_%s' % (expInfo['participant'], expInfo['participant'], expInfo['session'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/nj/Documents/Codes/Python/TriggerNotificationPython/tasks_psychopy.py',
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
    size=[4480, 1440], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start"
startClock = core.Clock()
# decide based on participant, session
task_type = participant_config.get_task_type(expInfo['participant'], expInfo['session'])
task_location = participant_config.get_task_location(expInfo['participant'], expInfo['session'])
task_mobility = participant_config.get_task_mobility(expInfo['participant'], expInfo['session'])
task_duration = participant_config.get_task_duration(expInfo['participant'], expInfo['session'])
notification_type = participant_config.get_notification_type(expInfo['participant'], expInfo['session'])
is_training_session = int(expInfo['session']) < 0

# get the notification list (to trigger  later)
notification_list = trigger_notification.get_notification_list(expInfo['participant'], expInfo['session'])

# log info
log_utility.log_participant_info(expInfo['participant'], expInfo['session'], task_type, task_location, task_mobility,notification_type)

# clear display
device_driver.clear_reading_passage()
device_driver.clear_notification_data()


txt_start = visual.TextStim(win=win, name='txt_start',
    text='Starting ...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "task_vigilance"
task_vigilanceClock = core.Clock()
trials_vigilance = 0

if task_type == 'vigilance':
   # enable trials
   trials_vigilance = 1
   
   # generate new stimuli
   stimuli_generation.generate_vigilance_stimuli_csv('stimuli/vigilance_stimuli.csv', task_duration)


# keep track of timing
timing_info = ''

# stimuli mapping
image_mapping = {'1': 'img/76x76.png',  '2':'img/100x100.png',  '3':'img/100x76.png', '4':'img/76x100.png'}

if task_location == 'desktop':
    # do nothing
    pass

if task_location == 'glass':
    # reset the stimuli mapping
   pass



mouse_v = event.Mouse(win=win)
x, y = [None, None]
mouse_v.mouseClock = core.Clock()
im_v = visual.ImageStim(
    win=win,
    name='im_v', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
im_line = visual.ImageStim(
    win=win,
    name='im_line', units='norm', 
    image='img/white_line.png', mask=None,
    ori=0, pos=(0, 0.35), size=(2, 0.005),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "task_reading"
task_readingClock = core.Clock()
reading_text = ''

trials_reading = 0

if task_type == 'reading':
    # enable trials
    trials_reading = 1
    

text_r = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(0, 0),     letterHeight=0.024,
     size=[1.25,None], borderWidth=1.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.03,
     anchor='center',
     fillColor='black', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='text_r',
     autoLog=True,
)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "task_recognition"
task_recognitionClock = core.Clock()
form_instr = visual.TextBox2(
     win, text='Have you seen the following notifications?\nCheck the whole sentence as some sentence may have altered the original notification.', font='Arial',
     pos=(0, 0.5),     letterHeight=0.025,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='top-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='form_instr',
     autoLog=True,
)
win.allowStencil = True
form_recog = visual.Form(win=win, name='form_recog',
    items='stimuli/recognition_stimuli.csv',
    textHeight=0.03,
    randomize=True,
    size=(1, 0.75),
    pos=(0, 0),
    style=['dark'],
    itemPadding=0.05,)

# Initialize components for Routine "end"
endClock = core.Clock()
txt_end = visual.TextStim(win=win, name='txt_end',
    text='Stopping ...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# start triggering notifications
trigger_notification.trigger_notification_randomly_threaded(expInfo['participant'], expInfo['session'], notification_list, globalClock)

# keep track of which components have finished
startComponents = [txt_start]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_start* updates
    if txt_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_start.frameNStart = frameN  # exact frame index
        txt_start.tStart = t  # local t and not account for scr refresh
        txt_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_start, 'tStartRefresh')  # time at next scr refresh
        txt_start.setAutoDraw(True)
    if txt_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt_start.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            txt_start.tStop = t  # not accounting for scr refresh
            txt_start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt_start, 'tStopRefresh')  # time at next scr refresh
            txt_start.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
log_utility.log_timing_threaded(expInfo['participant'], expInfo['session'], -1, globalClock.getTime(), win.getFutureFlipTime(clock=None))
thisExp.addData('txt_start.started', txt_start.tStartRefresh)
thisExp.addData('txt_start.stopped', txt_start.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_v = data.TrialHandler(nReps=trials_vigilance, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/vigilance_stimuli.csv'),
    seed=None, name='trials_v')
thisExp.addLoop(trials_v)  # add the loop to the experiment
thisTrials_v = trials_v.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_v.rgb)
if thisTrials_v != None:
    for paramName in thisTrials_v:
        exec('{} = thisTrials_v[paramName]'.format(paramName))

for thisTrials_v in trials_v:
    currentLoop = trials_v
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_v.rgb)
    if thisTrials_v != None:
        for paramName in thisTrials_v:
            exec('{} = thisTrials_v[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task_vigilance"-------
    continueRoutine = True
    routineTimer.add(0.625000)
    # update component parameters for each repeat
    timing_info = timing_info + '{},{},{}\n'.format(trials_v.thisRepN, globalClock.getTime(),  win.getFutureFlipTime(clock=None))
    # setup some python lists for storing info about the mouse_v
    mouse_v.x = []
    mouse_v.y = []
    mouse_v.leftButton = []
    mouse_v.midButton = []
    mouse_v.rightButton = []
    mouse_v.time = []
    gotValidClick = False  # until a click is received
    im_v.setImage(image_mapping[str(image_id)])
    # keep track of which components have finished
    task_vigilanceComponents = [mouse_v, im_v, im_line]
    for thisComponent in task_vigilanceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_vigilanceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task_vigilance"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = task_vigilanceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_vigilanceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_v* updates
        if mouse_v.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_v.frameNStart = frameN  # exact frame index
            mouse_v.tStart = t  # local t and not account for scr refresh
            mouse_v.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_v, 'tStartRefresh')  # time at next scr refresh
            mouse_v.status = STARTED
            prevButtonState = mouse_v.getPressed()  # if button is down already this ISN'T a new click
        if mouse_v.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_v.tStartRefresh + .625-frameTolerance:
                # keep track of stop time/frame for later
                mouse_v.tStop = t  # not accounting for scr refresh
                mouse_v.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_v, 'tStopRefresh')  # time at next scr refresh
                mouse_v.status = FINISHED
        if mouse_v.status == STARTED:  # only update if started and not finished!
            buttons = mouse_v.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_v.getPos()
                    mouse_v.x.append(x)
                    mouse_v.y.append(y)
                    buttons = mouse_v.getPressed()
                    mouse_v.leftButton.append(buttons[0])
                    mouse_v.midButton.append(buttons[1])
                    mouse_v.rightButton.append(buttons[2])
                    mouse_v.time.append(globalClock.getTime())
        
        # *im_v* updates
        if im_v.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im_v.frameNStart = frameN  # exact frame index
            im_v.tStart = t  # local t and not account for scr refresh
            im_v.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im_v, 'tStartRefresh')  # time at next scr refresh
            im_v.setAutoDraw(True)
        if im_v.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im_v.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                im_v.tStop = t  # not accounting for scr refresh
                im_v.frameNStop = frameN  # exact frame index
                win.timeOnFlip(im_v, 'tStopRefresh')  # time at next scr refresh
                im_v.setAutoDraw(False)
        
        # *im_line* updates
        if im_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im_line.frameNStart = frameN  # exact frame index
            im_line.tStart = t  # local t and not account for scr refresh
            im_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im_line, 'tStartRefresh')  # time at next scr refresh
            im_line.setAutoDraw(True)
        if im_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im_line.tStartRefresh + 0.625-frameTolerance:
                # keep track of stop time/frame for later
                im_line.tStop = t  # not accounting for scr refresh
                im_line.frameNStop = frameN  # exact frame index
                win.timeOnFlip(im_line, 'tStopRefresh')  # time at next scr refresh
                im_line.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_vigilanceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_vigilance"-------
    for thisComponent in task_vigilanceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_v (TrialHandler)
    trials_v.addData('mouse_v.x', mouse_v.x)
    trials_v.addData('mouse_v.y', mouse_v.y)
    trials_v.addData('mouse_v.leftButton', mouse_v.leftButton)
    trials_v.addData('mouse_v.midButton', mouse_v.midButton)
    trials_v.addData('mouse_v.rightButton', mouse_v.rightButton)
    trials_v.addData('mouse_v.time', mouse_v.time)
    trials_v.addData('mouse_v.started', mouse_v.tStartRefresh)
    trials_v.addData('mouse_v.stopped', mouse_v.tStopRefresh)
    trials_v.addData('im_v.started', im_v.tStartRefresh)
    trials_v.addData('im_v.stopped', im_v.tStopRefresh)
    trials_v.addData('im_line.started', im_line.tStartRefresh)
    trials_v.addData('im_line.stopped', im_line.tStopRefresh)
    thisExp.nextEntry()
    
# completed trials_vigilance repeats of 'trials_v'


# set up handler to look after randomisation of conditions etc
trials_r = data.TrialHandler(nReps=trials_reading, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_r')
thisExp.addLoop(trials_r)  # add the loop to the experiment
thisTrials_r = trials_r.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_r.rgb)
if thisTrials_r != None:
    for paramName in thisTrials_r:
        exec('{} = thisTrials_r[paramName]'.format(paramName))

for thisTrials_r in trials_r:
    currentLoop = trials_r
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_r.rgb)
    if thisTrials_r != None:
        for paramName in thisTrials_r:
            exec('{} = thisTrials_r[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task_reading"-------
    continueRoutine = True
    # update component parameters for each repeat
    # generate new text
    passage  = reading_passages.get_reading_passages(task_duration, is_training_session, expInfo['participant'])
    
    # log info
    log_utility.log_passage_info(expInfo['participant'], expInfo['session'], passage)
    
    # track time
    reading_start_time = globalClock.getTime()
    
    if task_location == 'desktop':
        # set text
        reading_text =  passage["text"]
    
    if task_location == 'glass':
        #clear the box
        text_r.fillColor = None
        # send text to glass
        device_driver.send_reading_passage(passage["text"])
        # enable scolling
        device_driver.enable_scrolling_listening()
    text_r.setText(reading_text)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    task_readingComponents = [text_r, key_resp]
    for thisComponent in task_readingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    task_readingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task_reading"-------
    while continueRoutine:
        # get current time
        t = task_readingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=task_readingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_r* updates
        if text_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_r.frameNStart = frameN  # exact frame index
            text_r.tStart = t  # local t and not account for scr refresh
            text_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_r, 'tStartRefresh')  # time at next scr refresh
            text_r.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_readingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task_reading"-------
    for thisComponent in task_readingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if task_location == 'glass':
        # clear text
        device_driver.clear_reading_passage()
        # disable scolling
        device_driver.disable_scrolling_listening()
    
    reading_text = ""
    
    # track time
    reading_end_time = globalClock.getTime()
    print('Reading time', reading_end_time - reading_start_time)
    trials_r.addData('text_r.started', text_r.tStartRefresh)
    trials_r.addData('text_r.stopped', text_r.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_r.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_r.addData('key_resp.rt', key_resp.rt)
    trials_r.addData('key_resp.started', key_resp.tStartRefresh)
    trials_r.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "task_reading" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trials_reading repeats of 'trials_r'


# ------Prepare to start Routine "task_recognition"-------
continueRoutine = True
# update component parameters for each repeat
# only allow to continue after fillign all questions
continueButton = visual.ButtonStim(win, labelText= "Continue", pos=(.35, -.45))

# cancel notification triggering
trigger_notification.cancel_notification_trigger()



# keep track of which components have finished
task_recognitionComponents = [form_instr, form_recog]
for thisComponent in task_recognitionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
task_recognitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "task_recognition"-------
while continueRoutine:
    # get current time
    t = task_recognitionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=task_recognitionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    continueButton.draw()
    
    if form_recog.complete:
        continueButton.buttonEnabled = True
        
    if continueButton.buttonSelected:
        continueRoutine = False
    
    # *form_instr* updates
    if form_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_instr.frameNStart = frameN  # exact frame index
        form_instr.tStart = t  # local t and not account for scr refresh
        form_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_instr, 'tStartRefresh')  # time at next scr refresh
        form_instr.setAutoDraw(True)
    
    # *form_recog* updates
    if form_recog.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_recog.frameNStart = frameN  # exact frame index
        form_recog.tStart = t  # local t and not account for scr refresh
        form_recog.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_recog, 'tStartRefresh')  # time at next scr refresh
        form_recog.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in task_recognitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "task_recognition"-------
for thisComponent in task_recognitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('form_instr.started', form_instr.tStartRefresh)
thisExp.addData('form_instr.stopped', form_instr.tStopRefresh)
form_recog.addDataToExp(thisExp, 'rows')
form_recog.autodraw = False
# the Routine "task_recognition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [txt_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
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
        if tThisFlipGlobal > txt_end.tStartRefresh + 1-frameTolerance:
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
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_end.started', txt_end.tStartRefresh)
thisExp.addData('txt_end.stopped', txt_end.tStopRefresh)
# log timing
log_utility.log_all_timing(expInfo['participant'], expInfo['session'], timing_info)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
