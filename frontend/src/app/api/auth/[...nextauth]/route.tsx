import NextAuth, { NextAuthOptions } from "next-auth"; 
import CredentialsProvider  from "next-auth/providers/credentials";
import GoogleProvider from "next-auth/providers/google";

  
  interface User {
    id: string;
  }
  

  
  export const authOptions: NextAuthOptions = {
    providers: [

      GoogleProvider({
        clientId:"762507943602-vrg24goe7lk4tlcmdj4t6bsa1ib0t13h.apps.googleusercontent.com",
        clientSecret: "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",
      }),
      CredentialsProvider({
        name: 'credentials',
        credentials: {},
        async authorize(credentials) {
          const user: User = { id: '1' };
          return user;
        },
      }),
    ],
    callbacks: {
        async signIn({ account,  user }) {
          
          // TODO: Implement this function to register the user with your own backend API.
         // await registerUser(user);
    
          return true;
        },
      },
    session: {
        strategy: "jwt",
    },
    secret: process.env.NEXTAUTH_SECRET,
    pages: {
        signIn: "/",
        signOut: "/"
    }
  };
const handler = NextAuth(authOptions) ;

export {handler as GET , handler as POST } ;
