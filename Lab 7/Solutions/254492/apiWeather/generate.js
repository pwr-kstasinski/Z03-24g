const openapi = require('openapi-client')
openapi.genCode({
  src: '../swagger.json',
  outDir: '../src/service',
  language: 'js',
})
.then(complete, error)
 
function complete(spec) {
  console.info('Service generation complete')
}
 
function error(e) {
  console.error(e.toString())
}