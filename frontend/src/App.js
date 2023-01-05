import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User";
import MenuList from "./components/Menu";
import FooterList from "./components/Footer";
import axios from 'axios';
import Footer from "./components/Footer";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }
// ОТРИСОВКА КОНТЕНТА
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(
            // === Получить от URL ответ и выполнить ==
            response => {
                const users = response.data
                this.setState({
                    'users': users
                })
            }
        ).catch(error => console.log(error)) // <== Иначе вывести ОШИТКУ в Консоль

    }

    render() {
        return (
            <div>
                <div>
                    <MenuList users={this.state}/>
                </div>
                <div>
                    <UserList users={this.state.users}/>
                </div>
                <div>
                    <FooterList users={this.state}/>
                </div>
            </div>
        )

    }
}

export default App;