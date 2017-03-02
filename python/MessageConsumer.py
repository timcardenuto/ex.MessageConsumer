#!/usr/bin/env python
#
#
# AUTO-GENERATED
#
# Source: ex.MessageConsumer.spd.xml
from ossie.resource import start_component
import logging
import sys

from MessageConsumer_base import *

class MessageConsumer_i(MessageConsumer_base):
    """<DESCRIPTION GOES HERE>"""
    def constructor(self):
        # When the input port receives a message that matches the message name and property structure, trigger a callback
        self.port_geo_in.registerMessage("geolocation", MessageConsumer_i.Geolocation, self.geoMsgCallback)
   
    def geoMsgCallback(self, msg_id, msg_value):
        print msg_id, msg_value
        print "\n"
        # TODO handle message
        sys.stdout.flush() 
          
    def process(self):
        # TODO fill in your code here
        self._log.debug("process() example log message")
        return NOOP

  
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.debug("Starting Component")
    start_component(MessageConsumer_i)

