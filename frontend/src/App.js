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
import CartPage from  './pages/cartpage/CartPage'

const App = () => {
  return (
    <BrowserRouter>
        <Header />
          <main className="py-3">
            <Container>
              <Routes>  
                <Route path="/" element={<HomePage />} exact />
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
