import { cn } from "@/lib/utils";
import Link from "next/link";
import React, { Children, HTMLAttributeAnchorTarget, ReactNode } from "react";

interface LinkButtonProps {
    href: any,
    target?: HTMLAttributeAnchorTarget | undefined,
    children: ReactNode,
    className?: String 
}


const LinkButtonSecondary: React.FC<LinkButtonProps> = ({  href, target ,children}) => {
    return <Link className="h-12 hover:bg-mentor/90 font-medium  text-white px-8 inline-flex items-center rounded-full justify-center whitespace-nowrap bg-mentor text-md  ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50" href={href} passHref target={target}>
        {children}
    </Link>;
}
const LinkButton: React.FC<LinkButtonProps> = ({  href, target ,children}) => {
    return <Link className="h-12 hover:bg-primary/80 font-medium  text-white px-8 inline-flex items-center rounded-full justify-center whitespace-nowrap bg-xmentor text-md  ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50" href={href} passHref target={target}>
        {children}
    </Link>;
}

const LinkButtonCircle: React.FC<LinkButtonProps> =({href , target , children }) => {
    return <Link className="h-12 hover:bg-gray-100  text-black px-8 inline-flex items-center rounded-full justify-center whitespace-nowrap  text-md  ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50" href={href} passHref target={target}>
         {children}
       <span className="h-2 w-2 ml-2  rounded-full bg-mentor ">
        
       </span>
    </Link> ;
}

const LinkButtonOutline: React.FC<LinkButtonProps> = ({href , target , children,className}) => {
    return  <Link className={cn("h-12 px-8 font-medium text-xmentor border border-xmentor bg-background hover:bg-accent hover:text-accent-foreground inline-flex items-center rounded-full justify-center whitespace-nowrap  text-md  ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
    className )} href={href} passHref target={target}>
    {children}
</Link>;
}

export  {LinkButton , LinkButtonCircle , LinkButtonOutline ,LinkButtonSecondary };