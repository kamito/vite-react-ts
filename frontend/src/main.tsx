import 'vite/modulepreload-polyfill'
import logger from 'js-logger'
import React from 'react'
import ReactDOM from 'react-dom/client'
import { ChakraProvider } from '@chakra-ui/react'
import { getInitData } from './const'
import App from './App'
import './index.css'

const isDebug = getInitData('IS_DEBUG')
const loglevel = (isDebug) ? logger.DEBUG : logger.INFO
logger.useDefaults()
logger.setLevel(loglevel)

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ChakraProvider>
      <App />
    </ChakraProvider>
  </React.StrictMode>
)
