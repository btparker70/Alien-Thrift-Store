import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Loader from '../../components/loader/Loader'
import Message from '../../components/message/Message'
import { login } from '../../actions/userActions'
import FormContainer from '../../components/formcontainer/FormContainer'

const LoginPage = () => {
  const [ email, setEmail ] = useState('')
  const [ password, setPassword ] = useState('')

  return (
    <FormContainer>
      Login Page
    </FormContainer>
  )
}

export default LoginPage