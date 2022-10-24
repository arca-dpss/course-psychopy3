/*************** 
 * Stroop Test *
 ***************/

import { core, data, sound, util, visual } from './lib/psychojs-2022.1.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'stroop';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '01'};

// Start code blocks for 'Before Experiment'
/* Syntax Error: Fix Python code */
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'norm',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(SETTINGRoutineBegin());
flowScheduler.add(SETTINGRoutineEachFrame());
flowScheduler.add(SETTINGRoutineEnd());
const HumanLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(HumanLoopLoopBegin(HumanLoopLoopScheduler));
flowScheduler.add(HumanLoopLoopScheduler);
flowScheduler.add(HumanLoopLoopEnd);
flowScheduler.add(MATRIXRoutineBegin());
flowScheduler.add(MATRIXRoutineEachFrame());
flowScheduler.add(MATRIXRoutineEnd());
const FullPracticeLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(FullPracticeLoopLoopBegin(FullPracticeLoopLoopScheduler));
flowScheduler.add(FullPracticeLoopLoopScheduler);
flowScheduler.add(FullPracticeLoopLoopEnd);
const ControbilanciamewntoLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ControbilanciamewntoLoopLoopBegin(ControbilanciamewntoLoopLoopScheduler));
flowScheduler.add(ControbilanciamewntoLoopLoopScheduler);
flowScheduler.add(ControbilanciamewntoLoopLoopEnd);
flowScheduler.add(LIKERTRoutineBegin());
flowScheduler.add(LIKERTRoutineEachFrame());
flowScheduler.add(LIKERTRoutineEnd());
flowScheduler.add(GRAZIERoutineBegin());
flowScheduler.add(GRAZIERoutineEachFrame());
flowScheduler.add(GRAZIERoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + (("data" + "/") + `${expInfo["participant"]}_${expInfo["date"]}`));

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var SETTINGClock;
var fixation_duration;
var rep_condition;
var num;
var nb_rep_ita;
var nb_rep_eng;
var blocco_order;
var HUMANClock;
var human_txt;
var math_txt;
var textbox;
var button;
var MATRIXClock;
var blue_img;
var red_img;
var practice_ms;
var ISTR_PRACTICEClock;
var istr_practice_txt;
var istr_practice_kb;
var FIXATIONClock;
var fixation_txt;
var TRIAL_PRACTICEClock;
var practice_txt;
var practice_kb;
var FEEDBACKClock;
var msg;
var endpractice;
var feedback_txt;
var ISTR_ESPERIMENTOClock;
var istr_esperimento_txt;
var istr_esperimento_kb;
var TRIAL_ITAClock;
var ita_txt;
var ita_kb;
var TRIAL_ENGClock;
var eng_txt;
var eng_kb;
var SWITCHClock;
var LIKERTClock;
var likert_txt;
var likert_sld;
var likert_bt;
var GRAZIEClock;
var logo_img;
var grazie_txt;
var grazie_kb;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "SETTING"
  SETTINGClock = new util.Clock();
  fixation_duration = 0.5;
  rep_condition = 1;
  num = (Number.parseInt(expInfo["participant"]) % 2);
  if ((num === 0)) {
      nb_rep_ita = (1 * rep_condition);
      nb_rep_eng = 0;
      blocco_order = "ITA_ENG";
  } else {
      nb_rep_eng = (1 * rep_condition);
      nb_rep_ita = 0;
      blocco_order = "ENG_ITA";
  }
  
  // Initialize components for Routine "HUMAN"
  HUMANClock = new util.Clock();
  human_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'human_txt',
    text: 'Scrivi il risultato:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  math_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'math_txt',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    font: 'Open Sans',
    pos: [0, (- 0.2)], letterHeight: 0.05,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  button = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button',
    text: 'validare',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.7)],
    letterHeight: 0.05,
    size: [0.2, 0.1]
  });
  button.clock = new util.Clock();
  
  // Initialize components for Routine "MATRIX"
  MATRIXClock = new util.Clock();
  blue_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'blue_img', units : 'pix', 
    image : 'images/blue_pill.jpg', mask : undefined,
    ori : 0.0, pos : [(- 250), 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  red_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'red_img', units : 'pix', 
    image : 'images/red_pill.jpg', mask : undefined,
    ori : 0.0, pos : [250, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  practice_ms = new core.Mouse({
    win: psychoJS.window,
  });
  practice_ms.mouseClock = new util.Clock();
  // Initialize components for Routine "ISTR_PRACTICE"
  ISTR_PRACTICEClock = new util.Clock();
  istr_practice_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'istr_practice_txt',
    text: "Per favore, premi la freccia;\nSINISTRA se il colore è ROSSO\nBASSA se il colore è VERDE\nDESTRA se il colore è BLU\n\nInitiamo con un po' di pratica\n\nPremi qualsiasi tasto per iniziare",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  istr_practice_kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FIXATION"
  FIXATIONClock = new util.Clock();
  fixation_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_txt',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TRIAL_PRACTICE"
  TRIAL_PRACTICEClock = new util.Clock();
  /* Syntax Error: Fix Python code */
  practice_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  practice_kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FEEDBACK"
  FEEDBACKClock = new util.Clock();
  msg = "";
  endpractice = [];
  
  feedback_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1, 1, 1]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "ISTR_ESPERIMENTO"
  ISTR_ESPERIMENTOClock = new util.Clock();
  istr_esperimento_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'istr_esperimento_txt',
    text: "Ottimo,\n\nAdesso iniziamo l'esperimento, ricordati di premere:\nSINISTRA se il colore è ROSSO\nBASSO se il colore è VERDE\nDESTRA se il colore è BLU\n\n\nPremi qualsiasi tasto per iniziare",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1, 1, 1]),  opacity: 1,
    depth: 0.0 
  });
  
  istr_esperimento_kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TRIAL_ITA"
  TRIAL_ITAClock = new util.Clock();
  /* Syntax Error: Fix Python code */
  ita_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'ita_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ita_kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TRIAL_ENG"
  TRIAL_ENGClock = new util.Clock();
  eng_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'eng_txt',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  eng_kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SWITCH"
  SWITCHClock = new util.Clock();
  // Initialize components for Routine "LIKERT"
  LIKERTClock = new util.Clock();
  likert_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'likert_txt',
    text: 'Da 1 a 10, quanto pensi di essere stato accurato nelle tue risposte ?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.5], height: 0.15,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  likert_sld = new visual.Slider({
    win: psychoJS.window, name: 'likert_sld',
    size: [1.0, 0.05], pos: [0, 0], units: 'norm',
    labels: ["per niente accurato", "molto accurato"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    granularity: 0.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  likert_bt = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'likert_bt',
    text: 'premi per prosseguire',
    fillColor: 'white',
    borderColor: null,
    color: 'black',
    colorSpace: 'rgb',
    pos: [0, (- 0.5)],
    letterHeight: 0.05,
    size: [0.3, 0.15]
  });
  likert_bt.clock = new util.Clock();
  
  // Initialize components for Routine "GRAZIE"
  GRAZIEClock = new util.Clock();
  logo_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'logo_img', units : 'pix', 
    image : 'images/logo.jpeg', mask : undefined,
    ori : 0.0, pos : [0, 150], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  grazie_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'grazie_txt',
    text: "L'esperimento è finito.\n\nGrazie!",
    font: 'arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1, 1, 1]),  opacity: 1,
    depth: -1.0 
  });
  
  grazie_kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var SETTINGComponents;
function SETTINGRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SETTING'-------
    t = 0;
    SETTINGClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    SETTINGComponents = [];
    
    for (const thisComponent of SETTINGComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SETTINGRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SETTING'-------
    // get current time
    t = SETTINGClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SETTINGComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SETTINGRoutineEnd() {
  return async function () {
    //------Ending Routine 'SETTING'-------
    for (const thisComponent of SETTINGComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "SETTING" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var HumanLoop;
var currentLoop;
function HumanLoopLoopBegin(HumanLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    HumanLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 100, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'HumanLoop'
    });
    psychoJS.experiment.addLoop(HumanLoop); // add the loop to the experiment
    currentLoop = HumanLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisHumanLoop of HumanLoop) {
      const snapshot = HumanLoop.getSnapshot();
      HumanLoopLoopScheduler.add(importConditions(snapshot));
      HumanLoopLoopScheduler.add(HUMANRoutineBegin(snapshot));
      HumanLoopLoopScheduler.add(HUMANRoutineEachFrame());
      HumanLoopLoopScheduler.add(HUMANRoutineEnd());
      HumanLoopLoopScheduler.add(endLoopIteration(HumanLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function HumanLoopLoopEnd() {
  psychoJS.experiment.removeLoop(HumanLoop);

  return Scheduler.Event.NEXT;
}


var FullPracticeLoop;
function FullPracticeLoopLoopBegin(FullPracticeLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    FullPracticeLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: practice, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'FullPracticeLoop'
    });
    psychoJS.experiment.addLoop(FullPracticeLoop); // add the loop to the experiment
    currentLoop = FullPracticeLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisFullPracticeLoop of FullPracticeLoop) {
      const snapshot = FullPracticeLoop.getSnapshot();
      FullPracticeLoopLoopScheduler.add(importConditions(snapshot));
      FullPracticeLoopLoopScheduler.add(ISTR_PRACTICERoutineBegin(snapshot));
      FullPracticeLoopLoopScheduler.add(ISTR_PRACTICERoutineEachFrame());
      FullPracticeLoopLoopScheduler.add(ISTR_PRACTICERoutineEnd());
      const PracticeLoopLoopScheduler = new Scheduler(psychoJS);
      FullPracticeLoopLoopScheduler.add(PracticeLoopLoopBegin(PracticeLoopLoopScheduler, snapshot));
      FullPracticeLoopLoopScheduler.add(PracticeLoopLoopScheduler);
      FullPracticeLoopLoopScheduler.add(PracticeLoopLoopEnd);
      FullPracticeLoopLoopScheduler.add(endLoopIteration(FullPracticeLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var PracticeLoop;
function PracticeLoopLoopBegin(PracticeLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    PracticeLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'condizione.xlsx',
      seed: undefined, name: 'PracticeLoop'
    });
    psychoJS.experiment.addLoop(PracticeLoop); // add the loop to the experiment
    currentLoop = PracticeLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPracticeLoop of PracticeLoop) {
      const snapshot = PracticeLoop.getSnapshot();
      PracticeLoopLoopScheduler.add(importConditions(snapshot));
      PracticeLoopLoopScheduler.add(FIXATIONRoutineBegin(snapshot));
      PracticeLoopLoopScheduler.add(FIXATIONRoutineEachFrame());
      PracticeLoopLoopScheduler.add(FIXATIONRoutineEnd());
      PracticeLoopLoopScheduler.add(TRIAL_PRACTICERoutineBegin(snapshot));
      PracticeLoopLoopScheduler.add(TRIAL_PRACTICERoutineEachFrame());
      PracticeLoopLoopScheduler.add(TRIAL_PRACTICERoutineEnd());
      PracticeLoopLoopScheduler.add(FEEDBACKRoutineBegin(snapshot));
      PracticeLoopLoopScheduler.add(FEEDBACKRoutineEachFrame());
      PracticeLoopLoopScheduler.add(FEEDBACKRoutineEnd());
      PracticeLoopLoopScheduler.add(endLoopIteration(PracticeLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function PracticeLoopLoopEnd() {
  psychoJS.experiment.removeLoop(PracticeLoop);

  return Scheduler.Event.NEXT;
}


async function FullPracticeLoopLoopEnd() {
  psychoJS.experiment.removeLoop(FullPracticeLoop);

  return Scheduler.Event.NEXT;
}


var ControbilanciamewntoLoop;
function ControbilanciamewntoLoopLoopBegin(ControbilanciamewntoLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ControbilanciamewntoLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'ControbilanciamewntoLoop'
    });
    psychoJS.experiment.addLoop(ControbilanciamewntoLoop); // add the loop to the experiment
    currentLoop = ControbilanciamewntoLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisControbilanciamewntoLoop of ControbilanciamewntoLoop) {
      const snapshot = ControbilanciamewntoLoop.getSnapshot();
      ControbilanciamewntoLoopLoopScheduler.add(importConditions(snapshot));
      ControbilanciamewntoLoopLoopScheduler.add(ISTR_ESPERIMENTORoutineBegin(snapshot));
      ControbilanciamewntoLoopLoopScheduler.add(ISTR_ESPERIMENTORoutineEachFrame());
      ControbilanciamewntoLoopLoopScheduler.add(ISTR_ESPERIMENTORoutineEnd());
      const ItaLoopLoopScheduler = new Scheduler(psychoJS);
      ControbilanciamewntoLoopLoopScheduler.add(ItaLoopLoopBegin(ItaLoopLoopScheduler, snapshot));
      ControbilanciamewntoLoopLoopScheduler.add(ItaLoopLoopScheduler);
      ControbilanciamewntoLoopLoopScheduler.add(ItaLoopLoopEnd);
      const EngLoopLoopScheduler = new Scheduler(psychoJS);
      ControbilanciamewntoLoopLoopScheduler.add(EngLoopLoopBegin(EngLoopLoopScheduler, snapshot));
      ControbilanciamewntoLoopLoopScheduler.add(EngLoopLoopScheduler);
      ControbilanciamewntoLoopLoopScheduler.add(EngLoopLoopEnd);
      ControbilanciamewntoLoopLoopScheduler.add(SWITCHRoutineBegin(snapshot));
      ControbilanciamewntoLoopLoopScheduler.add(SWITCHRoutineEachFrame());
      ControbilanciamewntoLoopLoopScheduler.add(SWITCHRoutineEnd());
      ControbilanciamewntoLoopLoopScheduler.add(endLoopIteration(ControbilanciamewntoLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var ItaLoop;
function ItaLoopLoopBegin(ItaLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ItaLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nb_rep_ita, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'condizione.xlsx',
      seed: undefined, name: 'ItaLoop'
    });
    psychoJS.experiment.addLoop(ItaLoop); // add the loop to the experiment
    currentLoop = ItaLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisItaLoop of ItaLoop) {
      const snapshot = ItaLoop.getSnapshot();
      ItaLoopLoopScheduler.add(importConditions(snapshot));
      ItaLoopLoopScheduler.add(FIXATIONRoutineBegin(snapshot));
      ItaLoopLoopScheduler.add(FIXATIONRoutineEachFrame());
      ItaLoopLoopScheduler.add(FIXATIONRoutineEnd());
      ItaLoopLoopScheduler.add(TRIAL_ITARoutineBegin(snapshot));
      ItaLoopLoopScheduler.add(TRIAL_ITARoutineEachFrame());
      ItaLoopLoopScheduler.add(TRIAL_ITARoutineEnd());
      ItaLoopLoopScheduler.add(endLoopIteration(ItaLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function ItaLoopLoopEnd() {
  psychoJS.experiment.removeLoop(ItaLoop);

  return Scheduler.Event.NEXT;
}


var EngLoop;
function EngLoopLoopBegin(EngLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    EngLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nb_rep_eng, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'condizione.xlsx',
      seed: undefined, name: 'EngLoop'
    });
    psychoJS.experiment.addLoop(EngLoop); // add the loop to the experiment
    currentLoop = EngLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisEngLoop of EngLoop) {
      const snapshot = EngLoop.getSnapshot();
      EngLoopLoopScheduler.add(importConditions(snapshot));
      EngLoopLoopScheduler.add(FIXATIONRoutineBegin(snapshot));
      EngLoopLoopScheduler.add(FIXATIONRoutineEachFrame());
      EngLoopLoopScheduler.add(FIXATIONRoutineEnd());
      EngLoopLoopScheduler.add(TRIAL_ENGRoutineBegin(snapshot));
      EngLoopLoopScheduler.add(TRIAL_ENGRoutineEachFrame());
      EngLoopLoopScheduler.add(TRIAL_ENGRoutineEnd());
      EngLoopLoopScheduler.add(endLoopIteration(EngLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function EngLoopLoopEnd() {
  psychoJS.experiment.removeLoop(EngLoop);

  return Scheduler.Event.NEXT;
}


async function ControbilanciamewntoLoopLoopEnd() {
  psychoJS.experiment.removeLoop(ControbilanciamewntoLoop);

  return Scheduler.Event.NEXT;
}


var x;
var y;
var correctsum;
var math;
var HUMANComponents;
function HUMANRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'HUMAN'-------
    t = 0;
    HUMANClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    x = Number.parseInt((Math.random() * 10));
    y = Number.parseInt((Math.random() * 10));
    correctsum = (x + y);
    math = (((x.toString() + " + ") + y.toString()) + " =");
    
    math_txt.setText(math);
    textbox.setText('');
    textbox.refresh();
    // keep track of which components have finished
    HUMANComponents = [];
    HUMANComponents.push(human_txt);
    HUMANComponents.push(math_txt);
    HUMANComponents.push(textbox);
    HUMANComponents.push(button);
    
    for (const thisComponent of HUMANComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function HUMANRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'HUMAN'-------
    // get current time
    t = HUMANClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    /* Syntax Error: Fix Python code */
    
    // *human_txt* updates
    if (t >= 0.0 && human_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      human_txt.tStart = t;  // (not accounting for frame time here)
      human_txt.frameNStart = frameN;  // exact frame index
      
      human_txt.setAutoDraw(true);
    }

    
    // *math_txt* updates
    if (t >= 0 && math_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      math_txt.tStart = t;  // (not accounting for frame time here)
      math_txt.frameNStart = frameN;  // exact frame index
      
      math_txt.setAutoDraw(true);
    }

    
    // *textbox* updates
    if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }

    
    // *button* updates
    if (t >= 0 && button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button.tStart = t;  // (not accounting for frame time here)
      button.frameNStart = frameN;  // exact frame index
      
      button.setAutoDraw(true);
    }

    if (button.status === PsychoJS.Status.STARTED) {
      // check whether button has been pressed
      if (button.isClicked) {
        if (!button.wasClicked) {
          // store time of first click
          button.timesOn.push(button.clock.getTime());
          button.numClicks += 1;
          // store time clicked until
          button.timesOff.push(button.clock.getTime());
        } else {
          // update time clicked until;
          button.timesOff[button.timesOff.length - 1] = button.clock.getTime();
        }
        if (!button.wasClicked) {
          // end routine when button is clicked
          continueRoutine = false;
          null;
        }
        // if button is still clicked next frame, it is not a new click
        button.wasClicked = true;
      } else {
        // if button is clicked next frame, it is a new click
        button.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button hasn't started / has finished
      button.clock.reset();
      // if button is clicked next frame, it is a new click
      button.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of HUMANComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function HUMANRoutineEnd() {
  return async function () {
    //------Ending Routine 'HUMAN'-------
    for (const thisComponent of HUMANComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((correctsum.toString() === textbox.text)) {
        HumanLoop.finished = true;
    }
    
    psychoJS.experiment.addData('textbox.text',textbox.text)
    psychoJS.experiment.addData('button.numClicks', button.numClicks);
    psychoJS.experiment.addData('button.timesOn', button.timesOn);
    psychoJS.experiment.addData('button.timesOff', button.timesOff);
    // the Routine "HUMAN" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var gotValidClick;
var MATRIXComponents;
function MATRIXRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'MATRIX'-------
    t = 0;
    MATRIXClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the practice_ms
    // current position of the mouse:
    practice_ms.x = [];
    practice_ms.y = [];
    practice_ms.leftButton = [];
    practice_ms.midButton = [];
    practice_ms.rightButton = [];
    practice_ms.time = [];
    practice_ms.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    MATRIXComponents = [];
    MATRIXComponents.push(blue_img);
    MATRIXComponents.push(red_img);
    MATRIXComponents.push(practice_ms);
    
    for (const thisComponent of MATRIXComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function MATRIXRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'MATRIX'-------
    // get current time
    t = MATRIXClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blue_img* updates
    if (t >= 0.0 && blue_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blue_img.tStart = t;  // (not accounting for frame time here)
      blue_img.frameNStart = frameN;  // exact frame index
      
      blue_img.setAutoDraw(true);
    }

    
    // *red_img* updates
    if (t >= 0.0 && red_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      red_img.tStart = t;  // (not accounting for frame time here)
      red_img.frameNStart = frameN;  // exact frame index
      
      red_img.setAutoDraw(true);
    }

    // *practice_ms* updates
    if (t >= 0.0 && practice_ms.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_ms.tStart = t;  // (not accounting for frame time here)
      practice_ms.frameNStart = frameN;  // exact frame index
      
      practice_ms.status = PsychoJS.Status.STARTED;
      practice_ms.mouseClock.reset();
      prevButtonState = practice_ms.getPressed();  // if button is down already this ISN'T a new click
      }
    if (practice_ms.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = practice_ms.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [blue_img, red_img]) {
            if (obj.contains(practice_ms)) {
              gotValidClick = true;
              practice_ms.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = practice_ms.getPos();
            practice_ms.x.push(_mouseXYs[0]);
            practice_ms.y.push(_mouseXYs[1]);
            practice_ms.leftButton.push(_mouseButtons[0]);
            practice_ms.midButton.push(_mouseButtons[1]);
            practice_ms.rightButton.push(_mouseButtons[2]);
            practice_ms.time.push(practice_ms.mouseClock.getTime());
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of MATRIXComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var practice;
function MATRIXRoutineEnd() {
  return async function () {
    //------Ending Routine 'MATRIX'-------
    for (const thisComponent of MATRIXComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((practice_ms.clicked_name[0] === "blue_img")) {
        practice = 1;
    } else {
        practice = 0;
    }
    
    // store data for psychoJS.experiment (ExperimentHandler)
    if (practice_ms.x) {  psychoJS.experiment.addData('practice_ms.x', practice_ms.x[0])};
    if (practice_ms.y) {  psychoJS.experiment.addData('practice_ms.y', practice_ms.y[0])};
    if (practice_ms.leftButton) {  psychoJS.experiment.addData('practice_ms.leftButton', practice_ms.leftButton[0])};
    if (practice_ms.midButton) {  psychoJS.experiment.addData('practice_ms.midButton', practice_ms.midButton[0])};
    if (practice_ms.rightButton) {  psychoJS.experiment.addData('practice_ms.rightButton', practice_ms.rightButton[0])};
    if (practice_ms.time) {  psychoJS.experiment.addData('practice_ms.time', practice_ms.time[0])};
    if (practice_ms.clicked_name) {  psychoJS.experiment.addData('practice_ms.clicked_name', practice_ms.clicked_name[0])};
    
    // the Routine "MATRIX" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _istr_practice_kb_allKeys;
var ISTR_PRACTICEComponents;
function ISTR_PRACTICERoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'ISTR_PRACTICE'-------
    t = 0;
    ISTR_PRACTICEClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    istr_practice_kb.keys = undefined;
    istr_practice_kb.rt = undefined;
    _istr_practice_kb_allKeys = [];
    // keep track of which components have finished
    ISTR_PRACTICEComponents = [];
    ISTR_PRACTICEComponents.push(istr_practice_txt);
    ISTR_PRACTICEComponents.push(istr_practice_kb);
    
    for (const thisComponent of ISTR_PRACTICEComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ISTR_PRACTICERoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'ISTR_PRACTICE'-------
    // get current time
    t = ISTR_PRACTICEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *istr_practice_txt* updates
    if (t >= 0.0 && istr_practice_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      istr_practice_txt.tStart = t;  // (not accounting for frame time here)
      istr_practice_txt.frameNStart = frameN;  // exact frame index
      
      istr_practice_txt.setAutoDraw(true);
    }

    
    // *istr_practice_kb* updates
    if (t >= 0.0 && istr_practice_kb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      istr_practice_kb.tStart = t;  // (not accounting for frame time here)
      istr_practice_kb.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      istr_practice_kb.clock.reset();
      istr_practice_kb.start();
      istr_practice_kb.clearEvents();
    }

    if (istr_practice_kb.status === PsychoJS.Status.STARTED) {
      let theseKeys = istr_practice_kb.getKeys({keyList: [], waitRelease: false});
      _istr_practice_kb_allKeys = _istr_practice_kb_allKeys.concat(theseKeys);
      if (_istr_practice_kb_allKeys.length > 0) {
        istr_practice_kb.keys = _istr_practice_kb_allKeys[_istr_practice_kb_allKeys.length - 1].name;  // just the last key pressed
        istr_practice_kb.rt = _istr_practice_kb_allKeys[_istr_practice_kb_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ISTR_PRACTICEComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISTR_PRACTICERoutineEnd() {
  return async function () {
    //------Ending Routine 'ISTR_PRACTICE'-------
    for (const thisComponent of ISTR_PRACTICEComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    istr_practice_kb.stop();
    // the Routine "ISTR_PRACTICE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var FIXATIONComponents;
function FIXATIONRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'FIXATION'-------
    t = 0;
    FIXATIONClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    FIXATIONComponents = [];
    FIXATIONComponents.push(fixation_txt);
    
    for (const thisComponent of FIXATIONComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function FIXATIONRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'FIXATION'-------
    // get current time
    t = FIXATIONClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_txt* updates
    if (t >= 0.0 && fixation_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_txt.tStart = t;  // (not accounting for frame time here)
      fixation_txt.frameNStart = frameN;  // exact frame index
      
      fixation_txt.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixation_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FIXATIONComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FIXATIONRoutineEnd() {
  return async function () {
    //------Ending Routine 'FIXATION'-------
    for (const thisComponent of FIXATIONComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "FIXATION" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _practice_kb_allKeys;
var TRIAL_PRACTICEComponents;
function TRIAL_PRACTICERoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'TRIAL_PRACTICE'-------
    t = 0;
    TRIAL_PRACTICEClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    practice_txt.setColor(new util.Color(colore));
    practice_txt.setText(parola);
    practice_kb.keys = undefined;
    practice_kb.rt = undefined;
    _practice_kb_allKeys = [];
    // keep track of which components have finished
    TRIAL_PRACTICEComponents = [];
    TRIAL_PRACTICEComponents.push(practice_txt);
    TRIAL_PRACTICEComponents.push(practice_kb);
    
    for (const thisComponent of TRIAL_PRACTICEComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TRIAL_PRACTICERoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'TRIAL_PRACTICE'-------
    // get current time
    t = TRIAL_PRACTICEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_txt* updates
    if (t >= 0 && practice_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_txt.tStart = t;  // (not accounting for frame time here)
      practice_txt.frameNStart = frameN;  // exact frame index
      
      practice_txt.setAutoDraw(true);
    }

    
    // *practice_kb* updates
    if (t >= 0 && practice_kb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_kb.tStart = t;  // (not accounting for frame time here)
      practice_kb.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practice_kb.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practice_kb.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practice_kb.clearEvents(); });
    }

    if (practice_kb.status === PsychoJS.Status.STARTED) {
      let theseKeys = practice_kb.getKeys({keyList: ['left', 'down', 'right'], waitRelease: false});
      _practice_kb_allKeys = _practice_kb_allKeys.concat(theseKeys);
      if (_practice_kb_allKeys.length > 0) {
        practice_kb.keys = _practice_kb_allKeys[_practice_kb_allKeys.length - 1].name;  // just the last key pressed
        practice_kb.rt = _practice_kb_allKeys[_practice_kb_allKeys.length - 1].rt;
        // was this correct?
        if (practice_kb.keys == corrAns) {
            practice_kb.corr = 1;
        } else {
            practice_kb.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TRIAL_PRACTICEComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TRIAL_PRACTICERoutineEnd() {
  return async function () {
    //------Ending Routine 'TRIAL_PRACTICE'-------
    for (const thisComponent of TRIAL_PRACTICEComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("blocco", "PRACTICE");
    psychoJS.experiment.addData("order", blocco_order);
    
    // was no response the correct answer?!
    if (practice_kb.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         practice_kb.corr = 1;  // correct non-response
      } else {
         practice_kb.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(practice_kb.corr, level);
    }
    psychoJS.experiment.addData('practice_kb.keys', practice_kb.keys);
    psychoJS.experiment.addData('practice_kb.corr', practice_kb.corr);
    if (typeof practice_kb.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practice_kb.rt', practice_kb.rt);
        routineTimer.reset();
        }
    
    practice_kb.stop();
    // the Routine "TRIAL_PRACTICE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var FEEDBACKComponents;
function FEEDBACKRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'FEEDBACK'-------
    t = 0;
    FEEDBACKClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if (practice_kb.corr) {
        msg = `Bravo! RT=${practice_kb.rt}`;
    } else {
        msg = "Oops! non \u00e8 coretto";
    }
    
    feedback_txt.setText(msg);
    // keep track of which components have finished
    FEEDBACKComponents = [];
    FEEDBACKComponents.push(feedback_txt);
    
    for (const thisComponent of FEEDBACKComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FEEDBACKRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'FEEDBACK'-------
    // get current time
    t = FEEDBACKClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_txt* updates
    if (t >= 0.0 && feedback_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_txt.tStart = t;  // (not accounting for frame time here)
      feedback_txt.frameNStart = frameN;  // exact frame index
      
      feedback_txt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FEEDBACKComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FEEDBACKRoutineEnd() {
  return async function () {
    //------Ending Routine 'FEEDBACK'-------
    for (const thisComponent of FEEDBACKComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    endpractice.push(practice_kb.corr);
    if ((util.sum(endpractice.slice((- 6))) === 4)) {
        PracticeLoop.finished = true;
    }
    
    return Scheduler.Event.NEXT;
  };
}


var _istr_esperimento_kb_allKeys;
var ISTR_ESPERIMENTOComponents;
function ISTR_ESPERIMENTORoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'ISTR_ESPERIMENTO'-------
    t = 0;
    ISTR_ESPERIMENTOClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    istr_esperimento_kb.keys = undefined;
    istr_esperimento_kb.rt = undefined;
    _istr_esperimento_kb_allKeys = [];
    // keep track of which components have finished
    ISTR_ESPERIMENTOComponents = [];
    ISTR_ESPERIMENTOComponents.push(istr_esperimento_txt);
    ISTR_ESPERIMENTOComponents.push(istr_esperimento_kb);
    
    for (const thisComponent of ISTR_ESPERIMENTOComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ISTR_ESPERIMENTORoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'ISTR_ESPERIMENTO'-------
    // get current time
    t = ISTR_ESPERIMENTOClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *istr_esperimento_txt* updates
    if (t >= 0 && istr_esperimento_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      istr_esperimento_txt.tStart = t;  // (not accounting for frame time here)
      istr_esperimento_txt.frameNStart = frameN;  // exact frame index
      
      istr_esperimento_txt.setAutoDraw(true);
    }

    
    // *istr_esperimento_kb* updates
    if (t >= 0 && istr_esperimento_kb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      istr_esperimento_kb.tStart = t;  // (not accounting for frame time here)
      istr_esperimento_kb.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      istr_esperimento_kb.clock.reset();
      istr_esperimento_kb.start();
      istr_esperimento_kb.clearEvents();
    }

    if (istr_esperimento_kb.status === PsychoJS.Status.STARTED) {
      let theseKeys = istr_esperimento_kb.getKeys({keyList: [], waitRelease: false});
      _istr_esperimento_kb_allKeys = _istr_esperimento_kb_allKeys.concat(theseKeys);
      if (_istr_esperimento_kb_allKeys.length > 0) {
        istr_esperimento_kb.keys = _istr_esperimento_kb_allKeys[_istr_esperimento_kb_allKeys.length - 1].name;  // just the last key pressed
        istr_esperimento_kb.rt = _istr_esperimento_kb_allKeys[_istr_esperimento_kb_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ISTR_ESPERIMENTOComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISTR_ESPERIMENTORoutineEnd() {
  return async function () {
    //------Ending Routine 'ISTR_ESPERIMENTO'-------
    for (const thisComponent of ISTR_ESPERIMENTOComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    istr_esperimento_kb.stop();
    // the Routine "ISTR_ESPERIMENTO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ita_kb_allKeys;
var TRIAL_ITAComponents;
function TRIAL_ITARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'TRIAL_ITA'-------
    t = 0;
    TRIAL_ITAClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ita_txt.setColor(new util.Color(colore));
    ita_txt.setText(parola);
    ita_kb.keys = undefined;
    ita_kb.rt = undefined;
    _ita_kb_allKeys = [];
    // keep track of which components have finished
    TRIAL_ITAComponents = [];
    TRIAL_ITAComponents.push(ita_txt);
    TRIAL_ITAComponents.push(ita_kb);
    
    for (const thisComponent of TRIAL_ITAComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TRIAL_ITARoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'TRIAL_ITA'-------
    // get current time
    t = TRIAL_ITAClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ita_txt* updates
    if (t >= 0 && ita_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ita_txt.tStart = t;  // (not accounting for frame time here)
      ita_txt.frameNStart = frameN;  // exact frame index
      
      ita_txt.setAutoDraw(true);
    }

    
    // *ita_kb* updates
    if (t >= 0 && ita_kb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ita_kb.tStart = t;  // (not accounting for frame time here)
      ita_kb.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ita_kb.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ita_kb.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ita_kb.clearEvents(); });
    }

    if (ita_kb.status === PsychoJS.Status.STARTED) {
      let theseKeys = ita_kb.getKeys({keyList: ['left', 'down', 'right'], waitRelease: false});
      _ita_kb_allKeys = _ita_kb_allKeys.concat(theseKeys);
      if (_ita_kb_allKeys.length > 0) {
        ita_kb.keys = _ita_kb_allKeys[_ita_kb_allKeys.length - 1].name;  // just the last key pressed
        ita_kb.rt = _ita_kb_allKeys[_ita_kb_allKeys.length - 1].rt;
        // was this correct?
        if (ita_kb.keys == corrAns) {
            ita_kb.corr = 1;
        } else {
            ita_kb.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TRIAL_ITAComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TRIAL_ITARoutineEnd() {
  return async function () {
    //------Ending Routine 'TRIAL_ITA'-------
    for (const thisComponent of TRIAL_ITAComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("blocco", "ITA");
    psychoJS.experiment.addData("order", blocco_order);
    
    // was no response the correct answer?!
    if (ita_kb.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         ita_kb.corr = 1;  // correct non-response
      } else {
         ita_kb.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(ita_kb.corr, level);
    }
    psychoJS.experiment.addData('ita_kb.keys', ita_kb.keys);
    psychoJS.experiment.addData('ita_kb.corr', ita_kb.corr);
    if (typeof ita_kb.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ita_kb.rt', ita_kb.rt);
        routineTimer.reset();
        }
    
    ita_kb.stop();
    // the Routine "TRIAL_ITA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _eng_kb_allKeys;
var TRIAL_ENGComponents;
function TRIAL_ENGRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'TRIAL_ENG'-------
    t = 0;
    TRIAL_ENGClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    eng_txt.setColor(new util.Color(colore));
    eng_txt.setText(word);
    eng_kb.keys = undefined;
    eng_kb.rt = undefined;
    _eng_kb_allKeys = [];
    // keep track of which components have finished
    TRIAL_ENGComponents = [];
    TRIAL_ENGComponents.push(eng_txt);
    TRIAL_ENGComponents.push(eng_kb);
    
    for (const thisComponent of TRIAL_ENGComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TRIAL_ENGRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'TRIAL_ENG'-------
    // get current time
    t = TRIAL_ENGClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *eng_txt* updates
    if (t >= 0.0 && eng_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eng_txt.tStart = t;  // (not accounting for frame time here)
      eng_txt.frameNStart = frameN;  // exact frame index
      
      eng_txt.setAutoDraw(true);
    }

    
    // *eng_kb* updates
    if (t >= 0.0 && eng_kb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eng_kb.tStart = t;  // (not accounting for frame time here)
      eng_kb.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { eng_kb.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { eng_kb.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { eng_kb.clearEvents(); });
    }

    if (eng_kb.status === PsychoJS.Status.STARTED) {
      let theseKeys = eng_kb.getKeys({keyList: ['left', 'down', 'right'], waitRelease: false});
      _eng_kb_allKeys = _eng_kb_allKeys.concat(theseKeys);
      if (_eng_kb_allKeys.length > 0) {
        eng_kb.keys = _eng_kb_allKeys[_eng_kb_allKeys.length - 1].name;  // just the last key pressed
        eng_kb.rt = _eng_kb_allKeys[_eng_kb_allKeys.length - 1].rt;
        // was this correct?
        if (eng_kb.keys == corrAns) {
            eng_kb.corr = 1;
        } else {
            eng_kb.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TRIAL_ENGComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TRIAL_ENGRoutineEnd() {
  return async function () {
    //------Ending Routine 'TRIAL_ENG'-------
    for (const thisComponent of TRIAL_ENGComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("blocco", "ENG");
    psychoJS.experiment.addData("order", blocco_order);
    
    // was no response the correct answer?!
    if (eng_kb.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         eng_kb.corr = 1;  // correct non-response
      } else {
         eng_kb.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(eng_kb.corr, level);
    }
    psychoJS.experiment.addData('eng_kb.keys', eng_kb.keys);
    psychoJS.experiment.addData('eng_kb.corr', eng_kb.corr);
    if (typeof eng_kb.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('eng_kb.rt', eng_kb.rt);
        routineTimer.reset();
        }
    
    eng_kb.stop();
    // the Routine "TRIAL_ENG" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var temp;
var SWITCHComponents;
function SWITCHRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SWITCH'-------
    t = 0;
    SWITCHClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    temp = nb_rep_ita;
    nb_rep_ita = nb_rep_eng;
    nb_rep_eng = temp;
    
    // keep track of which components have finished
    SWITCHComponents = [];
    
    for (const thisComponent of SWITCHComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SWITCHRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SWITCH'-------
    // get current time
    t = SWITCHClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SWITCHComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SWITCHRoutineEnd() {
  return async function () {
    //------Ending Routine 'SWITCH'-------
    for (const thisComponent of SWITCHComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "SWITCH" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var LIKERTComponents;
function LIKERTRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LIKERT'-------
    t = 0;
    LIKERTClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    likert_sld.reset()
    // keep track of which components have finished
    LIKERTComponents = [];
    LIKERTComponents.push(likert_txt);
    LIKERTComponents.push(likert_sld);
    LIKERTComponents.push(likert_bt);
    
    for (const thisComponent of LIKERTComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function LIKERTRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LIKERT'-------
    // get current time
    t = LIKERTClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *likert_txt* updates
    if (t >= 0.0 && likert_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      likert_txt.tStart = t;  // (not accounting for frame time here)
      likert_txt.frameNStart = frameN;  // exact frame index
      
      likert_txt.setAutoDraw(true);
    }

    
    // *likert_sld* updates
    if (t >= 0.0 && likert_sld.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      likert_sld.tStart = t;  // (not accounting for frame time here)
      likert_sld.frameNStart = frameN;  // exact frame index
      
      likert_sld.setAutoDraw(true);
    }

    
    // *likert_bt* updates
    if (t >= 0 && likert_bt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      likert_bt.tStart = t;  // (not accounting for frame time here)
      likert_bt.frameNStart = frameN;  // exact frame index
      
      likert_bt.setAutoDraw(true);
    }

    if (likert_bt.status === PsychoJS.Status.STARTED) {
      // check whether likert_bt has been pressed
      if (likert_bt.isClicked) {
        if (!likert_bt.wasClicked) {
          // store time of first click
          likert_bt.timesOn.push(likert_bt.clock.getTime());
          likert_bt.numClicks += 1;
          // store time clicked until
          likert_bt.timesOff.push(likert_bt.clock.getTime());
        } else {
          // update time clicked until;
          likert_bt.timesOff[likert_bt.timesOff.length - 1] = likert_bt.clock.getTime();
        }
        if (!likert_bt.wasClicked) {
          // end routine when likert_bt is clicked
          continueRoutine = false;
          null;
        }
        // if likert_bt is still clicked next frame, it is not a new click
        likert_bt.wasClicked = true;
      } else {
        // if likert_bt is clicked next frame, it is a new click
        likert_bt.wasClicked = false;
      }
    } else {
      // keep clock at 0 if likert_bt hasn't started / has finished
      likert_bt.clock.reset();
      // if likert_bt is clicked next frame, it is a new click
      likert_bt.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LIKERTComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LIKERTRoutineEnd() {
  return async function () {
    //------Ending Routine 'LIKERT'-------
    for (const thisComponent of LIKERTComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('likert_sld.response', likert_sld.getRating());
    psychoJS.experiment.addData('likert_sld.rt', likert_sld.getRT());
    psychoJS.experiment.addData('likert_bt.numClicks', likert_bt.numClicks);
    psychoJS.experiment.addData('likert_bt.timesOn', likert_bt.timesOn);
    psychoJS.experiment.addData('likert_bt.timesOff', likert_bt.timesOff);
    // the Routine "LIKERT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _grazie_kb_allKeys;
var GRAZIEComponents;
function GRAZIERoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'GRAZIE'-------
    t = 0;
    GRAZIEClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    grazie_kb.keys = undefined;
    grazie_kb.rt = undefined;
    _grazie_kb_allKeys = [];
    // keep track of which components have finished
    GRAZIEComponents = [];
    GRAZIEComponents.push(logo_img);
    GRAZIEComponents.push(grazie_txt);
    GRAZIEComponents.push(grazie_kb);
    
    for (const thisComponent of GRAZIEComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function GRAZIERoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'GRAZIE'-------
    // get current time
    t = GRAZIEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *logo_img* updates
    if (t >= 0.0 && logo_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      logo_img.tStart = t;  // (not accounting for frame time here)
      logo_img.frameNStart = frameN;  // exact frame index
      
      logo_img.setAutoDraw(true);
    }

    
    // *grazie_txt* updates
    if (t >= 0.0 && grazie_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      grazie_txt.tStart = t;  // (not accounting for frame time here)
      grazie_txt.frameNStart = frameN;  // exact frame index
      
      grazie_txt.setAutoDraw(true);
    }

    
    // *grazie_kb* updates
    if (t >= 0.0 && grazie_kb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      grazie_kb.tStart = t;  // (not accounting for frame time here)
      grazie_kb.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      grazie_kb.clock.reset();
      grazie_kb.start();
      grazie_kb.clearEvents();
    }

    if (grazie_kb.status === PsychoJS.Status.STARTED) {
      let theseKeys = grazie_kb.getKeys({keyList: [], waitRelease: false});
      _grazie_kb_allKeys = _grazie_kb_allKeys.concat(theseKeys);
      if (_grazie_kb_allKeys.length > 0) {
        grazie_kb.keys = _grazie_kb_allKeys[_grazie_kb_allKeys.length - 1].name;  // just the last key pressed
        grazie_kb.rt = _grazie_kb_allKeys[_grazie_kb_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of GRAZIEComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GRAZIERoutineEnd() {
  return async function () {
    //------Ending Routine 'GRAZIE'-------
    for (const thisComponent of GRAZIEComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    grazie_kb.stop();
    // the Routine "GRAZIE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
