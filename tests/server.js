const { exec, spawn } = require('child_process');
const { promisify } = require('util');

const execPromises = promisify(exec);

let isStarted = false;
let isStart = false;
let portNumber = null;

const execCommands = async (commands) => {
  const proc = await execPromises(commands).catch((err) => {
    if (err.stderr === '') return;
    console.error('Child Error!!!!!!!!: ', err.stderr);
    process.exit(1);
  });

  return proc?.stdout;
};

const spawnCommands = (cmd, opt) => {
  const spawned = spawn(cmd, opt);
  spawned.stdout.setEncoding('utf8');
  spawned.stdout.on('data', (data) => {
    if (!isStart && data.includes('Watching...')) {
      isStart = true;
      process.send({ isStart });
    }
  });
};

const killServer = async (_portNumber) => {
  const stdout = await execCommands(`lsof -i :${_portNumber}`);
  const stdoutArr = stdout.split('\n');
  const dataArr = stdoutArr[1].split(/\s+/);
  const serverPID = dataArr[1];
  process.kill(serverPID, 'SIGHUP');
};

process.on('message', async (message) => {
  if (!message?.portNumber) throw new Error('Port number is required!!!!!!!');

  const stdout = await execCommands(`lsof -i :${message.portNumber}`);
  portNumber = message.portNumber;
  if (stdout?.includes('LISTEN') && !isStart) {
    isStart = true;
    isStarted = true;
    process.send({ isStart });
  } else {
    spawnCommands('npm run start-server', { shell: true });
  }
});

process.on('SIGINT', async () => {
  if (!isStarted && isStart) await killServer(portNumber);
  process.send({ signal: 'SIGINT' });
  process.exit(0);
});

process.on('SIGHUP', async () => {
  if (!isStarted && isStart) await killServer(portNumber);
  process.send({ signal: 'SIGHUP' });
  process.exit(1);
});
