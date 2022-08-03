import _ from 'lodash'
import { Base64 } from 'js-base64'
import { InitData } from './@types/window.d'

const data: InitData = (() => {
  let data = window.$INIT
  if (!_.isEmpty(data)) {
    data = JSON.parse(Base64.decode(data))
  }
  return data
})()

export const getInitData: (k: string, defvar?: any) => any = (k, defvar = null) => {
  const v = _.get(data, k, defvar)
  return v
}

export const $INIT_DATA: InitData = data
