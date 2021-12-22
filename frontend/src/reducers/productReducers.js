// a reducer is a function that takes in
// the current state and an action of
// what is wanted to be done to the state
// then it changes and manipulates the state
// returns new copy of state into store
import {
  // ALL PRODUCT DATA
  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_LIST_FAIL,

  // SPECIFIC PRODUCT DATA
  PRODUCT_DETAILS_REQUEST,
  PRODUCT_DETAILS_SUCCESS,
  PRODUCT_DETAILS_FAIL
} from '../constants/productConstants'

// ALL PRODUCT DATA
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

// SPECIFIC PRODUCT DATA
export const productDetailsReducer = (state = { product: {reviews: []} }, action) => {
  switch(action.type) {
    case PRODUCT_DETAILS_REQUEST:
      return { loading: true, ...state }
      
    case PRODUCT_DETAILS_SUCCESS:
      return { loading: false, product: action.payload }

    case PRODUCT_DETAILS_FAIL:
      return { loading: false, error: action.payload }
    
    default: 
      return state
  }
}