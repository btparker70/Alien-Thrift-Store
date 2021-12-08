import "./App.css";
import { Container } from "react-bootstrap";

import Header from "./components/header/Header";
import Footer from "./components/footer/Footer";
import HomeScreen from "./pages/homescreen/HomeScreen";

function App() {
  return (
    <div>
      <Header />
      <main className="py-3">
        <Container>
          <HomeScreen />
        </Container>
      </main>
      <Footer />
    </div>
  );
}

export default App;
