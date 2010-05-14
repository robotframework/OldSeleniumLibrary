""" 
Flash Selenium - Python Client

Date: 30 March 2008
Paulo Caroli, Sachin Sudheendra
http://code.google.com/p/flash-selenium
-----------------------------------------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from selenium import selenium
from BrowserConstants import BrowserConstants

class FlashSelenium(object):
    
    def __init__(self, seleniumObj, flashObjectId):
        self.seleniumObj = seleniumObj
        self.flashObjectId = flashObjectId
        self.browserConstants = BrowserConstants();
        self.flashJSStringPrefix = self.createJSPrefix_document(self.flashObjectId)
        
    def start(self):
        self.seleniumObj.start()

    def stop(self):
        self.seleniumObj.stop()
        
    def open(self, Url):
        self.seleniumObj.open(Url)
    
    def call(self, functionName, *parameter):
        self.flashJSStringPrefix = self.checkBrowserAndReturnJSPrefix()
        return self.seleniumObj.get_eval(self.jsForFunction(functionName, list(parameter)))
    
    #### Standard Methods ####
    
    def percent_loaded(self):
        return self.call("PercentLoaded")
    
    def is_playing(self):
        return self.call("IsPlaying")
    
    def get_variable(self, varName):
        return self.call("GetVariable", varName)
    
    def goto_frame(self, value):
        return self.call("GotoFrame", value)
    
    def load_movie(self, layerNumber, Url):
        return self.call("LoadMovie", layerNumber, Url)
    
    def pan(self, x, y, mode):
        return self.call("Pan", x, y, mode)
    
    def play(self):
        return self.call("Play")
    
    def rewind(self):
        return self.call("Rewind")
    
    def set_variable(self, name, value):
        return self.call("SetVariable", name, value)
    
    def set_zoom_rect(self, left, top, right, bottom):
        return self.call("SetZoomRect", left, top, right, bottom)
    
    def stop_play(self):
        return self.call("StopPlay")
    
    def total_frames(self):
        return self.call("TotalFrames")
    
    def zoom(self, percent):
        return self.call("Zoom", percent)
    
    #### TellTarget Methods ####
    
    def t_call_frame(self, target, frameNumber):
        return self.call("TCallFrame", target, frameNumber)
    
    def t_call_label(self, target, label):
        return self.call("TCallLabel", target, label)
    
    def t_current_frame(self, target):
        return self.call("TCurrentFrame", target)
    
    def t_current_label(self, target):
        return self.call("TCurrentLabel", target)
    
    def t_get_property(self, target, property):
        return self.call("TGetProperty", target, property)

    def t_get_property_as_number(self, target, property):
        return self.call("TGetPropertyAsNumber", target, property)
    
    def t_goto_frame(self, target, frameNumber):
        return self.call("TGotoFrame", target, frameNumber)
    
    def t_goto_label(self, target, label):
        return self.call("TGotoLabel", target, label)
    
    def t_play(self, target):
        return self.call("TPlay", target)
    
    def t_set_property(self, property, value):
        return self.call("TSetProperty", property, value)
    
    def t_stop_play(self, target):
        return self.call("TStopPlay", target)
    
    #### Standard Events ####
    
    def on_progress(self, percent):
        return self.call("OnProgress", percent)
    
    def on_ready_state_change(self, state):
        return self.call("OnReadyStateChange", state)

    #### Custom Code ####
    
    def checkBrowserAndReturnJSPrefix(self):
        appName = self.seleniumObj.get_eval("navigator.userAgent")
        if (appName.find(self.browserConstants.firefox3()) is not -1) or (appName.find(self.browserConstants.msie()) is not -1):
            return self.createJSPrefix_window_document(self.flashObjectId)
        else:
            return self.createJSPrefix_document(self.flashObjectId)
        
    def createJSPrefix_window_document(self, flashObjectId):
        return "window.document['" + flashObjectId + "'].";
    
    def createJSPrefix_document(self, flashObjectId):
        return "document['" + flashObjectId + "'].";
    
    def jsForFunction(self, functionName, *args):
        functionArgs = ""
        if len(args) > 0 and args != None :
            for arg in args[0]:
                functionArgs = functionArgs + "'" + str(arg) + "',"
            functionArgs = functionArgs[0:len(functionArgs)-1]
        return self.flashJSStringPrefix + functionName + "(" + functionArgs + ");"