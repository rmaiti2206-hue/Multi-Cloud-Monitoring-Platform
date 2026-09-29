import React,{createContext,useContext,useState} from 'react';
import api from '../services/api';
const C=createContext(null);
export function AuthProvider({children}){const [user,setUser]=useState(()=>JSON.parse(localStorage.getItem('user')||'null'));const login=async(email,password)=>{const r=await api.post('/auth/login',{email,password});localStorage.setItem('access_token',r.data.access_token);localStorage.setItem('user',JSON.stringify(r.data.user));setUser(r.data.user)};const logout=()=>{localStorage.clear();setUser(null)};return <C.Provider value={{user,login,logout}}>{children}</C.Provider>};export const useAuth=()=>useContext(C);
