/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ericsson.dummyplugin.events.terminate;




/**
 *
 * @author Lenovo
 */
public class AppdTerminateReply {
    private long reqid;
    

    
    public AppdTerminateReply() {
        reqid = 0;
        
    }


    public AppdTerminateReply(long reqid) {
        this.reqid = reqid;
        
    }
    //insert set/get methods

    public long getReqid() {
        return reqid;
    }

    public void setReqid(long reqid) {
        this.reqid = reqid;
    }




}
