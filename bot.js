const Discord = require('discord.py');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    if (message.content === 'ping') {
    	message.reply('pong');
  	}
});

// THIS  MUST  BE  THIS  WAY
client.login(process.env.NDg3NzQ3OTU0MjA4MTQ1NDMz.Dnh0bQ.PFt6vftlewYPQejses00AoZvm6s);
