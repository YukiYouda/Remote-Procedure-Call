const net = require('net')
const socketPath = '/tmp/socket_file'

// UNIXドメインソケットを作成
const client = net.createConnection(socketPath, () => {
    console.log('connected to server');

    // サーバーにメッセージを送信
    const message = {
        method: 'validAnagram',
        params: ['test','sett'],
        param_types: ['string', 'string'],
        id: 2,
    };

    client.write(JSON.stringify(message));
});

// サーバーからのデータを受信
client.on('data', (data) => {
    console.log('Received : ', data.toString());
    client.end();
})

// サーバーからの接続終了通知を受信
client.on('end', () => {
    console.log('disconnected from server');
});
