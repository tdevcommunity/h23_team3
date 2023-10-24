import NextAuth, { NextAuthOptions } from "next-auth"; 
import CredentialsProvider  from "next-auth/providers/credentials";

  
  interface User {
    id: string;
  }
  

  
  export const authOptions: NextAuthOptions = {
    providers: [
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
        async signIn({ user }) {
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
