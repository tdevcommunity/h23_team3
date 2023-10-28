"use client"
import Link from 'next/link';
import Image from 'next/image';
import linksData from '@/data/links.json';
import { Key, useEffect, useRef, useState } from 'react';
import { Url } from 'url';
import { Button } from './button';
import {LinkButton, LinkButtonCircle} from './linkButton';
import { useSession, signIn, signOut } from "next-auth/react"
const Navbar = () => {
  const [scrolling , setScrolling] = useState(false);
  const links: {
    id: Key,
    name: String,
    url:  any,
    target: String
  }[] = linksData;
useEffect(() => {
  document.addEventListener('scroll', () => {
      setScrolling(window.scrollY > 120 );
  })
 

},[]) ;
  return (
    <nav className={` ${scrolling ? "bg-white/80 fade-in-70 duration-500 fixed  border-b" : ""}  bg-white  backdrop-blur-sm w-full z-30  `}>
      <div className="w-11/12 mx-auto flex items-center justify-between  duration-300  my-2">
        <div className="flex gap-10 ">
         <Link href={"/"} passHref >
           <Image
            src="/assets/logo/logo.png"
            className="my-2"
            alt="xmentor-logo"
            width={50}
            height={50}
          />
         </Link>
          <ul className="flex   gap-5  items-center">
            {links.map(link => <Link className='hover:text-xmentor duration-300 ' href={link.url} passHref key={link.id}> {link.name }</Link>)}
          </ul>
        </div>
        <div className="flex space-x-4 items-center">
  
        <LinkButtonCircle href={"/login"} target=''>
        Se connecter
        </LinkButtonCircle>
        <LinkButton  href={"register"} target=''>
          Inscription
        </LinkButton>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
