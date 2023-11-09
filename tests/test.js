const cp = require('child_process');
const { exec } = require('child_process');
const { promisify } = require('util');

const execPromises = promisify(exec);
const forked = cp.fork(`${__dirname}/server.js`);

const execCommands = (commands) => {
  execPromises(commands)
    .then(() => forked.kill('SIGINT'))
    .catch((err) => {
      if (err.stderr === '') {
        console.log('Parent Error???: ', err);
        return;
      }
      console.error('Parent Error!!!: ', err.stderr);
      forked.kill('SIGHUP');
    });
};

forked.on('message', (message) => {
  if (message.isStart) {
    execCommands('npm run test:unit');
  } else if (message.signal === 'SIGINT') {
    console.log('テスト成功！！！');
  } else if (message.signal === 'SIGHUP') {
    console.log('テスト失敗・・・');
    process.exit(1);
  }
});

forked.send({ portNumber: '3000' });
