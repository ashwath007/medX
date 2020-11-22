const express = require("express");
const app = express();


app.get("/", (req, res) => {
    res.send("Good")
})

app.listen(4000, () => {
    console.log('Server Listening');
})