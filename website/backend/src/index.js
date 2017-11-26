import express from 'express'
import bodyParser from 'body-parser'
import mysql from 'promise-mysql'
const settings = {
  host: 'localhost',
  user: 'root',
  password: 's7pXORZ123',
  database: 'smackdown'
}
const QUERY = `SELECT * FROM smackdown.posts ORDER BY RAND() LIMIT 5`

const app = express()
app.use(bodyParser.urlencoded({extended: true}))

app.get('/', (req, res) => {
  mysql.createConnection(settings)
    .then((conn) => {
      const result = conn.query(QUERY)
      conn.end()
      return result
    }).then((rows) => {
      res.send(rows)
    })
})

const server = app.listen(3001, () => {
  console.log('Server running at http://localhost:' + server.address().port)
})
