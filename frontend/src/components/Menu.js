import React from "react";


const MenuList = ({}) => {
    return(
        <div className="container">
            <header className="d-flex justify-content-center py-3">
                <ul className="nav nav-pills">
                    <li className="nav-item"><a href="#" className="nav-link active" aria-current="page">Пользователи</a></li>
                    <li className="nav-item"><a href="#" className="nav-link">Проекты</a></li>
                    <li className="nav-item"><a href="#" className="nav-link">Заметки</a></li>
                </ul>
            </header>
        </div>
    )
}

export default MenuList