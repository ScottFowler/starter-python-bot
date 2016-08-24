#!/usr/bin/env python

import logging
import os

from beepboop import resourcer
from beepboop import bot_manager

from slack_bot import SlackBot
from slack_bot import spawn_bot

logger = logging.getLogger(__name__)


if __name__ == "__main__":

    log_level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=log_level)

    slack_token = os.getenv("SLACK_TOKEN", "")
    logging.info("token: {}".format(slack_token))

    if slack_token == "":
        logging.info("SLACK_TOKEN env var not set, expecting token to be provided by Resourcer events")
        slack_token = None
        botManager = bot_manager.BotManager(spawn_bot)
        res = resourcer.Resourcer(botManager)
        res.start()
    else:
        var Botkit = require('botkit');

        var controller = Botkit.slackbot({
          debug: false
          //include "log: false" to disable logging
          //or a "logLevel" integer from 0 to 7 to adjust logging verbosity
        });
        
        // connect the bot to a stream of messages
        controller.spawn({
          token: <my_slack_bot_token>,
        }).startRTM()
        
        // give the bot something to listen for.
        controller.hears('hello',['direct_message','direct_mention','mention'],function(bot,message) {
        
          bot.reply(message,'Hello yourself.');
        
        });
        # only want to run a single instance of the bot in dev mode
        #bot = SlackBot(slack_token)
        #bot.start({})
