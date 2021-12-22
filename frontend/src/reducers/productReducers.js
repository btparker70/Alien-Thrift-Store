// a reducer is a function that takes in
// the current state and an action of
// what is wanted to be done to the state
// then it changes and manipulates the state
// returns new copy of state into store
import {
  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_LIST_FAIL
} from '../constants/productConstants'

export const productListReducer = (state = {products: [],}, action) => {
  switch(action.type) {
    case PRODUCT_LIST_REQUEST:
      return { loading: true, products: [] }
      
    case PRODUCT_LIST_SUCCESS:
      return { loading: false, products: action.payload }

    case PRODUCT_LIST_FAIL:
      return { loading: false, error: action.payload }
    
    default: 
      return state
  }
}