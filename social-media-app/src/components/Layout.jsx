import React, { createContext, useMemo, useState }from "react";
import Navigationbar from "./Navbar";
import Toaster from "./Toaster";

export const Context = createContext("unkown");

function Layout(props) {
  const [toaster, setToaster] = useState({
    title: "",
    show: false,
    message: "",
    type: "",
  });

  const value = useMemo(() => ({ toaster, setToaster}), [toaster]);


  return (
    <Context.Provider value={value}>
      <div>
        <Navigationbar />
        <div className="container m-5">{props.children}</div>
      </div>
      <Toaster
        title={toaster.title}
        message={toaster.message}
        type={toaster.type}
        showToast={toaster.show}
        onClose={() => setToaster({ ...toaster, show: false })}
      />
    </Context.Provider>
  );
}

export default Layout;
