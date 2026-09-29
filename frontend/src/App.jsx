import React from 'react';
import {Routes,Route,Navigate} from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import AWS from './pages/AWS';
import Azure from './pages/Azure';
import GCP from './pages/GCP';
import Resources from './pages/Resources';
import Metrics from './pages/Metrics';
import Alerts from './pages/Alerts';
import Accounts from './pages/Accounts';
import Users from './pages/Users';
import Reports from './pages/Reports';
import Settings from './pages/Settings';

function Layout({children}){return <><Navbar/><div className="layout"><Sidebar/><main>{children}</main></div></>}
export default function App(){
 const token=localStorage.getItem('token');
 return <Routes>
   <Route path="/login" element={<Login/>}/>
   <Route path="/" element={token?<Navigate to="/dashboard"/>:<Navigate to="/login"/>}/>
   {[
    ['/dashboard',Dashboard],['/aws',AWS],['/azure',Azure],['/gcp',GCP],
    ['/resources',Resources],['/metrics',Metrics],['/alerts',Alerts],
    ['/accounts',Accounts],['/users',Users],['/reports',Reports],['/settings',Settings]
   ].map(([p,C])=><Route key={p} path={p} element={<Layout><C/></Layout>}/>)}
 </Routes>
}