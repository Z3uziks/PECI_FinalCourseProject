import React, { useState } from 'react';
import MaterialDesignSwitch from "../../Components/Settings/MaterialDesignSwitch";
import PopupComponent from "../../Components/Settings/PopupComponent";

function Settings(){
    const [showPopup, setShowPopup] = useState(false);

    return(
        <div className=" w-11/12 mx-auto">
            <h1 className='my-3 text-2xl font-bold'>Notifications</h1>
            <MaterialDesignSwitch/>
            <div className="divider"></div>
            <a href="../../../../Log/index.html" target="_blank" style={{ backgroundColor: '#2693e6', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '5px', cursor: 'pointer', textDecoration: 'none' }}>About Us</a>
            <div className="divider"></div>
            <button
                style={{ backgroundColor: '#2693e6', color: 'white', padding: '10px', cursor: 'pointer', borderRadius: '5px' }}
                onClick={() => setShowPopup(true)}
            >
                Delete Account
            </button>
            {showPopup && <PopupComponent onClose={() => setShowPopup(false)} />}
            <div className="divider"></div>
        </div>
    )
}

export default Settings