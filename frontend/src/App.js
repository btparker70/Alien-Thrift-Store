import "./App.css";
import { Container } from "react-bootstrap";
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import Header from "./components/header/Header";
import Footer from "./components/footer/Footer";
import HomePage from "./pages/homepage/HomePage";
import ProductPage from "./pages/productpage/ProductPage";
import CartPage from  './pages/cartpage/CartPage';
import LoginPage from  './pages/loginpage/LoginPage';
import RegisterPage from  './pages/registerpage/RegisterPage';
import ProfilePage from  './pages/profilepage/ProfilePage';
import ShippingPage from  './pages/shippingpage/ShippingPage';

const App = () => {
  return (
    <BrowserRouter>
        <Header />
          <main className="py-3">
            <Container>
              <Routes>  
                <Route path="/" element={<HomePage />} exact />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/register" element={<RegisterPage />} />
                <Route path="/profile" element={<ProfilePage />} />
                <Route path="/shipping" element={<ShippingPage />} />
                <Route path="/product/:id" element={<ProductPage />} />
                {/* <Route path="/cart/:id/?" element={<CartPage />} /> */}
                <Route path="/cart" element={<CartPage />} >
                  <Route path=":id" element={<CartPage />} />
                </Route>
              </Routes>
            </Container>
          </main>
        <Footer />
    </BrowserRouter>
  );
}

export default App;
